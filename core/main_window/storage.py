# -*- coding: utf-8 -*-

"""This module contain the functions that main window needed."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2019"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from typing import (
    Tuple,
    Sequence,
    Dict,
    Optional,
)
from abc import ABC
from core.QtModules import (
    Slot,
    QApplication,
    QListWidgetItem,
    QInputDialog,
    QMessageBox,
)
from core.widgets import (
    AddStorage,
    DeleteStorage,
    AddStorageName,
    ClearStorageName,
)
from core.libs import parse_params
from .solver import SolverMethodInterface


class StorageMethodInterface(SolverMethodInterface, ABC):

    """Abstract class for storage methods."""

    def __add_storage(self, name: str, expr: str):
        """Add storage data function."""
        self.command_stack.beginMacro(f"Add {{Mechanism: {name}}}")
        self.command_stack.push(AddStorage(
            name,
            self.mechanism_storage,
            expr
        ))
        self.command_stack.endMacro()

    @Slot(name='on_mechanism_storage_add_clicked')
    def __add_current_storage(self):
        name = (
            self.mechanism_storage_name_tag.text() or
            self.mechanism_storage_name_tag.placeholderText()
        )
        self.command_stack.beginMacro(f"Add {{Mechanism: {name}}}")
        exprs = ", ".join(vpoint.expr() for vpoint in self.entities_point.data())
        self.__add_storage(name, f"M[{exprs}]")
        self.command_stack.push(ClearStorageName(self.mechanism_storage_name_tag))
        self.command_stack.endMacro()

    @Slot(name='on_mechanism_storage_copy_clicked')
    def __copy_storage(self):
        """Copy the expression from a storage data."""
        item = self.mechanism_storage.currentItem()
        if item:
            QApplication.clipboard().setText(item.expr)

    @Slot(name='on_mechanism_storage_paste_clicked')
    def __paste_storage(self):
        """Add the storage data from string."""
        expr, ok = QInputDialog.getMultiLineText(
            self,
            "Storage",
            "Please input expression:"
        )
        if not ok:
            return
        self.ask_add_storage(expr)

    def ask_add_storage(self, expr: str) -> bool:
        try:
            # Put the expression into parser to see if it is legal.
            parse_params(expr)
        except Exception as error:
            print(error)
            QMessageBox.warning(
                self,
                "Loading failed",
                "Your expression is in an incorrect format."
            )
            return False
        name, ok = QInputDialog.getText(
            self,
            "Storage",
            "Please input name tag:"
        )
        if not ok:
            return False
        name_list = [
            self.mechanism_storage.item(i).text()
            for i in range(self.mechanism_storage.count())
        ]
        i = 0
        name = name or f"Prototype_{i}"
        while name in name_list:
            name = f"Prototype_{i}"
            i += 1
        self.__add_storage(name, expr)
        return True

    @Slot(name='on_mechanism_storage_delete_clicked')
    def __delete_storage(self):
        """Delete the storage data."""
        row = self.mechanism_storage.currentRow()
        if not row > -1:
            return
        name = self.mechanism_storage.item(row).text()
        self.command_stack.beginMacro(f"Delete {{Mechanism: {name}}}")
        self.command_stack.push(DeleteStorage(row, self.mechanism_storage))
        self.command_stack.endMacro()

    @Slot(name='on_mechanism_storage_restore_clicked')
    @Slot(QListWidgetItem, name='on_mechanism_storage_itemDoubleClicked')
    def __restore_storage(self, item: Optional[QListWidgetItem] = None):
        """Restore the storage data."""
        if item is None:
            item = self.mechanism_storage.currentItem()
        if not item:
            return

        if QMessageBox.question(
            self,
            "Storage",
            "Restore mechanism will overwrite the canvas.\n"
            "Do you want to continue?"
        ) != QMessageBox.Yes:
            return

        name = item.text()
        self.command_stack.beginMacro(f"Restore from {{Mechanism: {name}}}")

        # After saved storage, clean all the item of two table widgets.
        self.entities_point.clear()
        self.entities_link.clear()
        self.inputs_widget.variable_excluding()

        self.parse_expression(item.expr)
        self.command_stack.push(DeleteStorage(
            self.mechanism_storage.row(item),
            self.mechanism_storage
        ))
        self.command_stack.push(AddStorageName(name, self.mechanism_storage_name_tag))
        self.command_stack.endMacro()
        self.main_canvas.zoom_to_fit()

    def get_storage(self) -> Dict[str, str]:
        """Get storage data."""
        storage: Dict[str, str] = {}
        for row in range(self.mechanism_storage.count()):
            item: QListWidgetItem = self.mechanism_storage.item(row)
            storage[item.text()] = item.expr
        return storage

    def add_multiple_storage(self, exprs: Sequence[Tuple[str, str]]):
        """Add storage data from database."""
        for name, expr in exprs:
            self.__add_storage(name, expr)
