# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ahshoe\Desktop\Pyslvs-PyQt5\core\synthesis\Collections\TriangularIteration_dialog\customs.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(343, 627)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/collection-triangular-iteration.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.new_group = QtWidgets.QGroupBox(Dialog)
        self.new_group.setObjectName("new_group")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.new_group)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.custom_list = QtWidgets.QListWidget(self.new_group)
        self.custom_list.setObjectName("custom_list")
        self.horizontalLayout_3.addWidget(self.custom_list)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.link_choose_label = QtWidgets.QLabel(self.new_group)
        self.link_choose_label.setObjectName("link_choose_label")
        self.verticalLayout.addWidget(self.link_choose_label)
        self.link_choose = QtWidgets.QComboBox(self.new_group)
        self.link_choose.setObjectName("link_choose")
        self.verticalLayout.addWidget(self.link_choose)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.add_button = QtWidgets.QPushButton(self.new_group)
        self.add_button.setObjectName("add_button")
        self.verticalLayout.addWidget(self.add_button)
        self.delete_button = QtWidgets.QPushButton(self.new_group)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_button.setIcon(icon1)
        self.delete_button.setObjectName("delete_button")
        self.verticalLayout.addWidget(self.delete_button)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.new_group)
        self.multiple_group = QtWidgets.QGroupBox(Dialog)
        self.multiple_group.setObjectName("multiple_group")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.multiple_group)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.multiple_list = QtWidgets.QListWidget(self.multiple_group)
        self.multiple_list.setObjectName("multiple_list")
        self.horizontalLayout_2.addWidget(self.multiple_list)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.quote_choose_label = QtWidgets.QLabel(self.multiple_group)
        self.quote_choose_label.setObjectName("quote_choose_label")
        self.verticalLayout_2.addWidget(self.quote_choose_label)
        self.quote_choose = QtWidgets.QComboBox(self.multiple_group)
        self.quote_choose.setObjectName("quote_choose")
        self.verticalLayout_2.addWidget(self.quote_choose)
        self.quote_link_choose_label = QtWidgets.QLabel(self.multiple_group)
        self.quote_link_choose_label.setObjectName("quote_link_choose_label")
        self.verticalLayout_2.addWidget(self.quote_link_choose_label)
        self.quote_link_choose = QtWidgets.QComboBox(self.multiple_group)
        self.quote_link_choose.setObjectName("quote_link_choose")
        self.verticalLayout_2.addWidget(self.quote_link_choose)
        self.joint_choose_label = QtWidgets.QLabel(self.multiple_group)
        self.joint_choose_label.setObjectName("joint_choose_label")
        self.verticalLayout_2.addWidget(self.joint_choose_label)
        self.joint_choose = QtWidgets.QComboBox(self.multiple_group)
        self.joint_choose.setObjectName("joint_choose")
        self.verticalLayout_2.addWidget(self.joint_choose)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.add_mj_button = QtWidgets.QPushButton(self.multiple_group)
        self.add_mj_button.setObjectName("add_mj_button")
        self.verticalLayout_2.addWidget(self.add_mj_button)
        self.delete_mj_button = QtWidgets.QPushButton(self.multiple_group)
        self.delete_mj_button.setIcon(icon1)
        self.delete_mj_button.setObjectName("delete_mj_button")
        self.verticalLayout_2.addWidget(self.delete_mj_button)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addWidget(self.multiple_group)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Custom joints"))
        self.new_group.setTitle(_translate("Dialog", "New joints"))
        self.link_choose_label.setText(_translate("Dialog", "Belong with:"))
        self.add_button.setText(_translate("Dialog", "Add"))
        self.delete_button.setText(_translate("Dialog", "Delete"))
        self.multiple_group.setTitle(_translate("Dialog", "Multiple joints"))
        self.quote_choose_label.setText(_translate("Dialog", "Quoted from:"))
        self.quote_link_choose_label.setText(_translate("Dialog", "Belong with:"))
        self.joint_choose_label.setText(_translate("Dialog", "Joint:"))
        self.add_mj_button.setText(_translate("Dialog", "Add"))
        self.delete_mj_button.setText(_translate("Dialog", "Delete"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

