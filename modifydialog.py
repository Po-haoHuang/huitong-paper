# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modifydialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ModifyDialog(object):
    def setupUi(self, ModifyDialog):
        ModifyDialog.setObjectName(_fromUtf8("ModifyDialog"))
        ModifyDialog.resize(236, 130)
        self.resultbuttonBox = QtGui.QDialogButtonBox(ModifyDialog)
        self.resultbuttonBox.setGeometry(QtCore.QRect(80, 70, 81, 32))
        self.resultbuttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.resultbuttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.resultbuttonBox.setObjectName(_fromUtf8("resultbuttonBox"))
        self.deletecheckBox = QtGui.QCheckBox(ModifyDialog)
        self.deletecheckBox.setGeometry(QtCore.QRect(150, 20, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deletecheckBox.setFont(font)
        self.deletecheckBox.setObjectName(_fromUtf8("deletecheckBox"))
        self.transferpushButton = QtGui.QPushButton(ModifyDialog)
        self.transferpushButton.setGeometry(QtCore.QRect(50, 30, 61, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(10)
        self.transferpushButton.setFont(font)
        self.transferpushButton.setObjectName(_fromUtf8("transferpushButton"))

        self.retranslateUi(ModifyDialog)
        QtCore.QObject.connect(self.resultbuttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ModifyDialog.accept)
        QtCore.QObject.connect(self.resultbuttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ModifyDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ModifyDialog)

    def retranslateUi(self, ModifyDialog):
        ModifyDialog.setWindowTitle(_translate("ModifyDialog", "Dialog", None))
        self.deletecheckBox.setText(_translate("ModifyDialog", "刪除", None))
        self.transferpushButton.setText(_translate("ModifyDialog", "入庫", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ModifyDialog = QtGui.QDialog()
    ui = Ui_ModifyDialog()
    ui.setupUi(ModifyDialog)
    ModifyDialog.show()
    sys.exit(app.exec_())

