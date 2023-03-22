# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'predict_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_predict_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(421, 213)
        Dialog.setStyleSheet("QDialog{\n"
"    background-color: #1b1b27;\n"
"}\n"
"#pred_label, #feedback_edit{\n"
"    color: rgb(255, 170, 0);\n"
"}\n"
"#feedback_edit, #pred_edit{\n"
"    background-color: transparent;\n"
"}\n"
"#pred_edit{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pred_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        font.setBold(True)
        self.pred_label.setFont(font)
        self.pred_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pred_label.setObjectName("pred_label")
        self.verticalLayout.addWidget(self.pred_label, 0, QtCore.Qt.AlignTop)
        self.feedback_edit = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feedback_edit.sizePolicy().hasHeightForWidth())
        self.feedback_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.feedback_edit.setFont(font)
        self.feedback_edit.setText("")
        self.feedback_edit.setFrame(False)
        self.feedback_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.feedback_edit.setObjectName("feedback_edit")
        self.verticalLayout.addWidget(self.feedback_edit)
        self.pred_edit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        font.setBold(True)
        self.pred_edit.setFont(font)
        self.pred_edit.setFrame(False)
        self.pred_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.pred_edit.setObjectName("pred_edit")
        self.verticalLayout.addWidget(self.pred_edit)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pred_label.setText(_translate("Dialog", "Predicted Health Status"))
        self.feedback_edit.setPlaceholderText(_translate("Dialog", "This where you can see the feedback"))
        self.pred_edit.setPlaceholderText(_translate("Dialog", "Prediction Result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
