# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_report_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(426, 239)
        Dialog.setStyleSheet("QDialog{background-color: #1b1b27;}\n"
"#report_table{background-color: #27263c; color: rgb(255, 255, 255);}\n"
"QHeaderView::section {background-color: rgb(170, 170, 255);}\n"
"QTableCornerButton::section { background-color:rgb(170, 170, 255);}\n"
"QTableView::item:selected {color:white; background:#000000; font-weight:900;}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.report_table = QtWidgets.QTableWidget(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.report_table.setFont(font)
        self.report_table.setAutoFillBackground(False)
        self.report_table.setFrameShape(QtWidgets.QFrame.Box)
        self.report_table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.report_table.setGridStyle(QtCore.Qt.SolidLine)
        self.report_table.setObjectName("report_table")
        self.report_table.setColumnCount(4)
        self.report_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.report_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.report_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.report_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.report_table.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.report_table)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.del_Btn = QtWidgets.QPushButton(self.frame)
        self.del_Btn.setObjectName("del_Btn")
        self.horizontalLayout.addWidget(self.del_Btn)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">Plant Health Report</span></p></body></html>"))
        item = self.report_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Plant ID"))
        item = self.report_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Date"))
        item = self.report_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Time"))
        item = self.report_table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Plant Health Status"))
        self.del_Btn.setText(_translate("Dialog", "Delete"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
