# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyslvs_ui/widgets/inputs.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from qtpy import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(309, 580)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/motor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tab_widget = QtWidgets.QTabWidget(Form)
        self.tab_widget.setObjectName("tab_widget")
        self.inputs_tab = QtWidgets.QWidget()
        self.inputs_tab.setObjectName("inputs_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.inputs_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.joint_groupbox = QtWidgets.QGroupBox(self.inputs_tab)
        self.joint_groupbox.setObjectName("joint_groupbox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.joint_groupbox)
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.joint_list_lable = QtWidgets.QLabel(self.joint_groupbox)
        self.joint_list_lable.setObjectName("joint_list_lable")
        self.verticalLayout_13.addWidget(self.joint_list_lable)
        self.joint_list = QtWidgets.QListWidget(self.joint_groupbox)
        self.joint_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.joint_list.setObjectName("joint_list")
        self.verticalLayout_13.addWidget(self.joint_list)
        self.horizontalLayout.addLayout(self.verticalLayout_13)
        self.inputs_label_right2 = QtWidgets.QLabel(self.joint_groupbox)
        self.inputs_label_right2.setObjectName("inputs_label_right2")
        self.horizontalLayout.addWidget(self.inputs_label_right2)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.driver_list_lable = QtWidgets.QLabel(self.joint_groupbox)
        self.driver_list_lable.setObjectName("driver_list_lable")
        self.verticalLayout_16.addWidget(self.driver_list_lable)
        self.driver_list = QtWidgets.QListWidget(self.joint_groupbox)
        self.driver_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.driver_list.setObjectName("driver_list")
        self.verticalLayout_16.addWidget(self.driver_list)
        self.variable_add = QtWidgets.QPushButton(self.joint_groupbox)
        self.variable_add.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/arrow_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.variable_add.setIcon(icon1)
        self.variable_add.setObjectName("variable_add")
        self.verticalLayout_16.addWidget(self.variable_add)
        self.horizontalLayout.addLayout(self.verticalLayout_16)
        self.verticalLayout.addWidget(self.joint_groupbox)
        self.variable_groupbox = QtWidgets.QGroupBox(self.inputs_tab)
        self.variable_groupbox.setObjectName("variable_groupbox")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.variable_groupbox)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.variable_up = QtWidgets.QPushButton(self.variable_groupbox)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/arrow_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.variable_up.setIcon(icon2)
        self.variable_up.setObjectName("variable_up")
        self.horizontalLayout_2.addWidget(self.variable_up)
        self.variable_down = QtWidgets.QPushButton(self.variable_groupbox)
        self.variable_down.setIcon(icon1)
        self.variable_down.setObjectName("variable_down")
        self.horizontalLayout_2.addWidget(self.variable_down)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.variable_remove = QtWidgets.QPushButton(self.variable_groupbox)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.variable_remove.setIcon(icon3)
        self.variable_remove.setObjectName("variable_remove")
        self.horizontalLayout_2.addWidget(self.variable_remove)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.variable_list = QtWidgets.QListWidget(self.variable_groupbox)
        self.variable_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.variable_list.setObjectName("variable_list")
        self.verticalLayout_5.addWidget(self.variable_list)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.line_5 = QtWidgets.QFrame(self.variable_groupbox)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_7.addWidget(self.line_5)
        self.inputs_dial_layout = QtWidgets.QVBoxLayout()
        self.inputs_dial_layout.setObjectName("inputs_dial_layout")
        self.dial_spinbox = QtWidgets.QDoubleSpinBox(self.variable_groupbox)
        self.dial_spinbox.setEnabled(False)
        self.dial_spinbox.setMaximum(360.0)
        self.dial_spinbox.setObjectName("dial_spinbox")
        self.inputs_dial_layout.addWidget(self.dial_spinbox)
        self.update_pos = QtWidgets.QPushButton(self.variable_groupbox)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/translate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_pos.setIcon(icon4)
        self.update_pos.setObjectName("update_pos")
        self.inputs_dial_layout.addWidget(self.update_pos)
        self.horizontalLayout_7.addLayout(self.inputs_dial_layout)
        self.verticalLayout.addWidget(self.variable_groupbox)
        self.groupBox = QtWidgets.QGroupBox(self.inputs_tab)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.variable_speed_label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.variable_speed_label.sizePolicy().hasHeightForWidth())
        self.variable_speed_label.setSizePolicy(sizePolicy)
        self.variable_speed_label.setObjectName("variable_speed_label")
        self.horizontalLayout_4.addWidget(self.variable_speed_label)
        self.variable_speed = QtWidgets.QSpinBox(self.groupBox)
        self.variable_speed.setEnabled(False)
        self.variable_speed.setMinimum(-100)
        self.variable_speed.setMaximum(100)
        self.variable_speed.setSingleStep(5)
        self.variable_speed.setProperty("value", -10)
        self.variable_speed.setObjectName("variable_speed")
        self.horizontalLayout_4.addWidget(self.variable_speed)
        self.verticalLayout_18.addLayout(self.horizontalLayout_4)
        self.extremeRebound = QtWidgets.QCheckBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extremeRebound.sizePolicy().hasHeightForWidth())
        self.extremeRebound.setSizePolicy(sizePolicy)
        self.extremeRebound.setChecked(True)
        self.extremeRebound.setObjectName("extremeRebound")
        self.verticalLayout_18.addWidget(self.extremeRebound)
        self.horizontalLayout_3.addLayout(self.verticalLayout_18)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.variable_play = QtWidgets.QPushButton(self.groupBox)
        self.variable_play.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.variable_play.sizePolicy().hasHeightForWidth())
        self.variable_play.setSizePolicy(sizePolicy)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(":/icons/pause.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.variable_play.setIcon(icon5)
        self.variable_play.setCheckable(True)
        self.variable_play.setObjectName("variable_play")
        self.verticalLayout_3.addWidget(self.variable_play)
        self.variable_stop = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.variable_stop.sizePolicy().hasHeightForWidth())
        self.variable_stop.setSizePolicy(sizePolicy)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/interrupted.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.variable_stop.setIcon(icon6)
        self.variable_stop.setObjectName("variable_stop")
        self.verticalLayout_3.addWidget(self.variable_stop)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.tab_widget.addTab(self.inputs_tab, icon, "")
        self.analysis_tab = QtWidgets.QWidget()
        self.analysis_tab.setObjectName("analysis_tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.analysis_tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.record_show = QtWidgets.QCheckBox(self.analysis_tab)
        self.record_show.setChecked(True)
        self.record_show.setObjectName("record_show")
        self.horizontalLayout_6.addWidget(self.record_show)
        self.show_all_button = QtWidgets.QPushButton(self.analysis_tab)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/merge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show_all_button.setIcon(icon7)
        self.show_all_button.setObjectName("show_all_button")
        self.horizontalLayout_6.addWidget(self.show_all_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.record_interval_label = QtWidgets.QLabel(self.analysis_tab)
        self.record_interval_label.setObjectName("record_interval_label")
        self.horizontalLayout_6.addWidget(self.record_interval_label)
        self.record_interval = QtWidgets.QDoubleSpinBox(self.analysis_tab)
        self.record_interval.setDecimals(2)
        self.record_interval.setMinimum(0.01)
        self.record_interval.setMaximum(6.0)
        self.record_interval.setProperty("value", 1.0)
        self.record_interval.setObjectName("record_interval")
        self.horizontalLayout_6.addWidget(self.record_interval)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.record_list = QtWidgets.QListWidget(self.analysis_tab)
        self.record_list.setObjectName("record_list")
        self.horizontalLayout_8.addWidget(self.record_list)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.update_preview_button = QtWidgets.QPushButton(self.analysis_tab)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/data_update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_preview_button.setIcon(icon8)
        self.update_preview_button.setObjectName("update_preview_button")
        self.verticalLayout_2.addWidget(self.update_preview_button)
        self.copy_path = QtWidgets.QPushButton(self.analysis_tab)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copy_path.setIcon(icon9)
        self.copy_path.setObjectName("copy_path")
        self.verticalLayout_2.addWidget(self.copy_path)
        self.record_start = QtWidgets.QPushButton(self.analysis_tab)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/record.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.record_start.setIcon(icon10)
        self.record_start.setCheckable(True)
        self.record_start.setObjectName("record_start")
        self.verticalLayout_2.addWidget(self.record_start)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.record_remove = QtWidgets.QPushButton(self.analysis_tab)
        self.record_remove.setIcon(icon3)
        self.record_remove.setObjectName("record_remove")
        self.verticalLayout_2.addWidget(self.record_remove)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.plot_joint = QtWidgets.QComboBox(self.analysis_tab)
        self.plot_joint.setObjectName("plot_joint")
        self.horizontalLayout_5.addWidget(self.plot_joint)
        self.plot_button = QtWidgets.QPushButton(self.analysis_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_button.sizePolicy().hasHeightForWidth())
        self.plot_button.setSizePolicy(sizePolicy)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/formula.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plot_button.setIcon(icon11)
        self.plot_button.setObjectName("plot_button")
        self.horizontalLayout_5.addWidget(self.plot_button)
        self.show_button = QtWidgets.QPushButton(self.analysis_tab)
        self.show_button.setIcon(icon7)
        self.show_button.setObjectName("show_button")
        self.horizontalLayout_5.addWidget(self.show_button)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.cp_data_button = QtWidgets.QPushButton(self.analysis_tab)
        self.cp_data_button.setIcon(icon9)
        self.cp_data_button.setObjectName("cp_data_button")
        self.verticalLayout_6.addWidget(self.cp_data_button)
        self.plot_groupbox = QtWidgets.QGroupBox(self.analysis_tab)
        self.plot_groupbox.setObjectName("plot_groupbox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.plot_groupbox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.wrt_label = QtWidgets.QCheckBox(self.plot_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wrt_label.sizePolicy().hasHeightForWidth())
        self.wrt_label.setSizePolicy(sizePolicy)
        self.wrt_label.setObjectName("wrt_label")
        self.horizontalLayout_10.addWidget(self.wrt_label)
        self.wrt_joint = QtWidgets.QComboBox(self.plot_groupbox)
        self.wrt_joint.setObjectName("wrt_joint")
        self.horizontalLayout_10.addWidget(self.wrt_joint)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.c_coord_sys = QtWidgets.QRadioButton(self.plot_groupbox)
        self.c_coord_sys.setChecked(True)
        self.c_coord_sys.setObjectName("c_coord_sys")
        self.horizontalLayout_11.addWidget(self.c_coord_sys)
        self.p_coord_sys = QtWidgets.QRadioButton(self.plot_groupbox)
        self.p_coord_sys.setObjectName("p_coord_sys")
        self.horizontalLayout_11.addWidget(self.p_coord_sys)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.plot_jerk = QtWidgets.QCheckBox(self.plot_groupbox)
        self.plot_jerk.setObjectName("plot_jerk")
        self.gridLayout.addWidget(self.plot_jerk, 3, 0, 1, 1)
        self.plot_vel = QtWidgets.QCheckBox(self.plot_groupbox)
        self.plot_vel.setObjectName("plot_vel")
        self.gridLayout.addWidget(self.plot_vel, 1, 0, 1, 1)
        self.plot_acc = QtWidgets.QCheckBox(self.plot_groupbox)
        self.plot_acc.setObjectName("plot_acc")
        self.gridLayout.addWidget(self.plot_acc, 2, 0, 1, 1)
        self.plot_pos = QtWidgets.QCheckBox(self.plot_groupbox)
        self.plot_pos.setChecked(True)
        self.plot_pos.setObjectName("plot_pos")
        self.gridLayout.addWidget(self.plot_pos, 0, 0, 1, 1)
        self.plot_curvature = QtWidgets.QCheckBox(self.plot_groupbox)
        self.plot_curvature.setObjectName("plot_curvature")
        self.gridLayout.addWidget(self.plot_curvature, 0, 1, 1, 1)
        self.plot_signature = QtWidgets.QCheckBox(self.plot_groupbox)
        self.plot_signature.setObjectName("plot_signature")
        self.gridLayout.addWidget(self.plot_signature, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout_6.addWidget(self.plot_groupbox)
        self.tab_widget.addTab(self.analysis_tab, icon11, "")
        self.verticalLayout_8.addWidget(self.tab_widget)

        self.retranslateUi(Form)
        self.record_list.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.joint_groupbox.setTitle(_translate("Form", "Inputs"))
        self.joint_list_lable.setText(_translate("Form", "Base points"))
        self.joint_list.setStatusTip(_translate("Form", "Choose a point to be a revolute joint."))
        self.inputs_label_right2.setText(_translate("Form", ">>"))
        self.driver_list_lable.setText(_translate("Form", "Driver points"))
        self.driver_list.setStatusTip(_translate("Form", "Coordinate movement reference."))
        self.variable_add.setStatusTip(_translate("Form", "Add to variable list with above settings."))
        self.variable_groupbox.setTitle(_translate("Form", "Variables"))
        self.variable_up.setStatusTip(_translate("Form", "Upgrade priority of the variable."))
        self.variable_down.setStatusTip(_translate("Form", "Downgrade priority of the variable."))
        self.variable_remove.setStatusTip(_translate("Form", "Delete the specified variable."))
        self.variable_list.setStatusTip(_translate("Form", "All the variable of this mechanism."))
        self.dial_spinbox.setStatusTip(_translate("Form", "Current position of the variable."))
        self.dial_spinbox.setSuffix(_translate("Form", "°"))
        self.update_pos.setStatusTip(_translate("Form", "Update current position as point coordinates."))
        self.update_pos.setText(_translate("Form", "Set pos"))
        self.groupBox.setTitle(_translate("Form", "Control"))
        self.variable_speed_label.setText(_translate("Form", "Speed:"))
        self.variable_speed.setStatusTip(_translate("Form", "Speed value of the auto driver."))
        self.variable_speed.setSuffix(_translate("Form", " rpm"))
        self.extremeRebound.setStatusTip(_translate("Form", "When solver calls error, auto driver will change the direction."))
        self.extremeRebound.setText(_translate("Form", "Extreme rebound"))
        self.variable_play.setStatusTip(_translate("Form", "Start / Pause the auto driver of this variables."))
        self.variable_stop.setStatusTip(_translate("Form", "Stop the auto driver and return to original place."))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.inputs_tab), _translate("Form", "Inputs"))
        self.record_show.setStatusTip(_translate("Form", "Show path data on the canvas."))
        self.record_show.setText(_translate("Form", "Show path data"))
        self.show_all_button.setText(_translate("Form", "Show all"))
        self.record_interval_label.setText(_translate("Form", "Interval:"))
        self.record_interval.setStatusTip(_translate("Form", "Each coordinate will be recorded after this angle value."))
        self.record_interval.setSuffix(_translate("Form", "°"))
        self.record_list.setStatusTip(_translate("Form", "All recorded path data of this project."))
        self.update_preview_button.setStatusTip(_translate("Form", "Refresh preview path data."))
        self.copy_path.setStatusTip(_translate("Form", "Duplicate the current paths with a new name."))
        self.record_start.setStatusTip(_translate("Form", "Start / Stop record."))
        self.record_remove.setStatusTip(_translate("Form", "Delete the specified path data."))
        self.plot_button.setStatusTip(_translate("Form", "Plot the data of this joint."))
        self.plot_button.setText(_translate("Form", "Plot"))
        self.show_button.setStatusTip(_translate("Form", "Show this joint only."))
        self.show_button.setText(_translate("Form", "Show only"))
        self.cp_data_button.setStatusTip(_translate("Form", "Copy the data of this joint to clipboard."))
        self.cp_data_button.setText(_translate("Form", "Copy data"))
        self.plot_groupbox.setTitle(_translate("Form", "Plot"))
        self.wrt_label.setText(_translate("Form", "With respect to:"))
        self.c_coord_sys.setText(_translate("Form", "Cartesian coordinates"))
        self.p_coord_sys.setText(_translate("Form", "Polar coordinates"))
        self.plot_jerk.setText(_translate("Form", "Jerk"))
        self.plot_vel.setText(_translate("Form", "Velocity"))
        self.plot_acc.setText(_translate("Form", "Acceleration"))
        self.plot_pos.setText(_translate("Form", "Position"))
        self.plot_curvature.setText(_translate("Form", "Curvature"))
        self.plot_signature.setText(_translate("Form", "Path Signature"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.analysis_tab), _translate("Form", "Analysis"))
from pyslvs_ui import icons_rc
