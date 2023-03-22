# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_6.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 270)
        MainWindow.setStyleSheet("#logo{background-color: transparent;}\n"
"#LeftMenu,#centralwidget{background-color: #1b1b27;}\n"
"#header, #mainBody{background-color: #27263c;}\n"
"#ip_label, #cam_select_label,#plant_id_label{color: rgb(255, 255, 255);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(4, 0, 4, 4)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QWidget(self.centralwidget)
        self.header.setMinimumSize(QtCore.QSize(0, 0))
        self.header.setMaximumSize(QtCore.QSize(16777215, 25))
        self.header.setObjectName("header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout.setContentsMargins(0, 2, 0, 2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo_frame = QtWidgets.QFrame(self.header)
        self.logo_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logo_frame.setObjectName("logo_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.logo_frame)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_label = QtWidgets.QLabel(self.logo_frame)
        self.logo_label.setMinimumSize(QtCore.QSize(20, 20))
        self.logo_label.setStyleSheet("background-image: url(:/newPrefix/icons/PIQlogo5.png);")
        self.logo_label.setText("")
        self.logo_label.setObjectName("logo_label")
        self.horizontalLayout_3.addWidget(self.logo_label)
        self.app_name_label = QtWidgets.QLabel(self.logo_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.app_name_label.setFont(font)
        self.app_name_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.app_name_label.setObjectName("app_name_label")
        self.horizontalLayout_3.addWidget(self.app_name_label)
        self.horizontalLayout.addWidget(self.logo_frame, 0, QtCore.Qt.AlignLeft)
        self.frame_2 = QtWidgets.QFrame(self.header)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.header)
        self.mainBody = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.mainBody.setObjectName("mainBody")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mainBody)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LeftMenu = QtWidgets.QWidget(self.mainBody)
        self.LeftMenu.setMinimumSize(QtCore.QSize(0, 0))
        self.LeftMenu.setMaximumSize(QtCore.QSize(50, 16777215))
        self.LeftMenu.setObjectName("LeftMenu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.LeftMenu)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.captureBtn = QtWidgets.QPushButton(self.LeftMenu)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.captureBtn.setFont(font)
        self.captureBtn.setObjectName("captureBtn")
        self.verticalLayout_2.addWidget(self.captureBtn)
        self.predictBtn = QtWidgets.QPushButton(self.LeftMenu)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.predictBtn.setFont(font)
        self.predictBtn.setObjectName("predictBtn")
        self.verticalLayout_2.addWidget(self.predictBtn)
        self.reportBtn = QtWidgets.QPushButton(self.LeftMenu)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.reportBtn.setFont(font)
        self.reportBtn.setObjectName("reportBtn")
        self.verticalLayout_2.addWidget(self.reportBtn)
        self.helpBtn = QtWidgets.QPushButton(self.LeftMenu)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.helpBtn.setFont(font)
        self.helpBtn.setObjectName("helpBtn")
        self.verticalLayout_2.addWidget(self.helpBtn)
        self.plant_id_label = QtWidgets.QLabel(self.LeftMenu)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.plant_id_label.setFont(font)
        self.plant_id_label.setObjectName("plant_id_label")
        self.verticalLayout_2.addWidget(self.plant_id_label)
        self.plant_id_edit = QtWidgets.QComboBox(self.LeftMenu)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.plant_id_edit.setFont(font)
        self.plant_id_edit.setFont(font)
        self.plant_id_edit.setEditable(True)
        self.plant_id_edit.setCurrentText("")
        self.plant_id_edit.setMaxVisibleItems(4)
        self.plant_id_edit.setFrame(True)
        self.plant_id_edit.setObjectName("plant_id_edit")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")
        self.plant_id_edit.addItem("")

        #ADDED
        font = QtGui.QFont('Segoe UI', 6)
        plant_id_font_edit = self.plant_id_edit.lineEdit()
        plant_id_font_edit.setFont(font)

        self.verticalLayout_2.addWidget(self.plant_id_edit)
        self.ip_label = QtWidgets.QLabel(self.LeftMenu)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.ip_label.setFont(font)
        self.ip_label.setObjectName("ip_label")
        self.verticalLayout_2.addWidget(self.ip_label)
        self.ip_edit = QtWidgets.QComboBox(self.LeftMenu)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.ip_edit.setFont(font)
        self.ip_edit.setEditable(True)
        self.ip_edit.setMaxVisibleItems(4)
        self.ip_edit.setObjectName("ip_edit")
        self.ip_edit.addItem("")
        self.ip_edit.addItem("")

        #ADDED
        font = QtGui.QFont('Segoe UI', 6)
        ip_font_edit = self.ip_edit.lineEdit()
        ip_font_edit.setFont(font)

        self.verticalLayout_2.addWidget(self.ip_edit)
        spacerItem = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.LeftMenu, 0, QtCore.Qt.AlignLeft)
        self.RightMenu = QtWidgets.QWidget(self.mainBody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RightMenu.sizePolicy().hasHeightForWidth())
        self.RightMenu.setSizePolicy(sizePolicy)
        self.RightMenu.setObjectName("RightMenu")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.RightMenu)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cam_feed_frame = QtWidgets.QFrame(self.RightMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cam_feed_frame.sizePolicy().hasHeightForWidth())
        self.cam_feed_frame.setSizePolicy(sizePolicy)
        self.cam_feed_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cam_feed_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cam_feed_frame.setObjectName("cam_feed_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.cam_feed_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        self.cam_feed_label = QtWidgets.QLabel(self.cam_feed_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cam_feed_label.sizePolicy().hasHeightForWidth())
        self.cam_feed_label.setSizePolicy(sizePolicy)
        self.cam_feed_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cam_feed_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cam_feed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cam_feed_label.setObjectName("cam_feed_label")

        self.verticalLayout_3.addWidget(self.cam_feed_label)
        self.verticalLayout_4.addWidget(self.cam_feed_frame)
        self.horizontalLayout_2.addWidget(self.RightMenu)
        self.verticalLayout.addWidget(self.mainBody)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.plant_id_edit.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.app_name_label.setText(_translate("MainWindow", "PechayIQ App"))
        self.captureBtn.setText(_translate("MainWindow", "Capture"))
        self.predictBtn.setText(_translate("MainWindow", "Predict"))
        self.reportBtn.setText(_translate("MainWindow", "Report"))
        self.helpBtn.setText(_translate("MainWindow", "Help"))
        self.plant_id_label.setText(_translate("MainWindow", "Plant ID:"))
        self.plant_id_edit.setItemText(0, _translate("MainWindow", "A1"))
        self.plant_id_edit.setItemText(1, _translate("MainWindow", "A2"))
        self.plant_id_edit.setItemText(2, _translate("MainWindow", "A3"))
        self.plant_id_edit.setItemText(3, _translate("MainWindow", "A4"))
        self.plant_id_edit.setItemText(4, _translate("MainWindow", "A5"))
        self.plant_id_edit.setItemText(5, _translate("MainWindow", "A6"))
        self.plant_id_edit.setItemText(6, _translate("MainWindow", "A7"))
        self.plant_id_edit.setItemText(7, _translate("MainWindow", "A8"))
        self.plant_id_edit.setItemText(8, _translate("MainWindow", "A9"))
        self.plant_id_edit.setItemText(9, _translate("MainWindow", "A10"))
        self.plant_id_edit.setItemText(10, _translate("MainWindow", "B1"))
        self.plant_id_edit.setItemText(11, _translate("MainWindow", "B2"))
        self.plant_id_edit.setItemText(12, _translate("MainWindow", "B3"))
        self.plant_id_edit.setItemText(13, _translate("MainWindow", "B4"))
        self.plant_id_edit.setItemText(14, _translate("MainWindow", "B5"))
        self.plant_id_edit.setItemText(15, _translate("MainWindow", "B6"))
        self.plant_id_edit.setItemText(16, _translate("MainWindow", "B7"))
        self.plant_id_edit.setItemText(17, _translate("MainWindow", "B8"))
        self.plant_id_edit.setItemText(18, _translate("MainWindow", "B9"))
        self.plant_id_edit.setItemText(19, _translate("MainWindow", "B10"))
        self.plant_id_edit.setItemText(20, _translate("MainWindow", "C1"))
        self.plant_id_edit.setItemText(21, _translate("MainWindow", "C2"))
        self.plant_id_edit.setItemText(22, _translate("MainWindow", "C3"))
        self.plant_id_edit.setItemText(23, _translate("MainWindow", "C4"))
        self.plant_id_edit.setItemText(24, _translate("MainWindow", "C5"))
        self.plant_id_edit.setItemText(25, _translate("MainWindow", "C6"))
        self.plant_id_edit.setItemText(26, _translate("MainWindow", "C7"))
        self.plant_id_edit.setItemText(27, _translate("MainWindow", "C8"))
        self.plant_id_edit.setItemText(28, _translate("MainWindow", "C9"))
        self.plant_id_edit.setItemText(29, _translate("MainWindow", "C10"))
        self.plant_id_edit.setItemText(30, _translate("MainWindow", "D1"))
        self.plant_id_edit.setItemText(31, _translate("MainWindow", "D2"))
        self.plant_id_edit.setItemText(32, _translate("MainWindow", "D3"))
        self.plant_id_edit.setItemText(33, _translate("MainWindow", "D4"))
        self.plant_id_edit.setItemText(34, _translate("MainWindow", "D5"))
        self.plant_id_edit.setItemText(35, _translate("MainWindow", "D6"))
        self.plant_id_edit.setItemText(36, _translate("MainWindow", "D7"))
        self.plant_id_edit.setItemText(37, _translate("MainWindow", "D8"))
        self.plant_id_edit.setItemText(38, _translate("MainWindow", "D9"))
        self.plant_id_edit.setItemText(39, _translate("MainWindow", "D10"))
        self.ip_label.setText(_translate("MainWindow", "Server IP:"))
        self.ip_edit.setItemText(0, _translate("MainWindow", "192.168.50.117"))
        self.ip_edit.setItemText(1, _translate("MainWindow", "192.168.204.118"))
        self.cam_feed_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Image Feed</span></p></body></html>"))
import test_rc


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())