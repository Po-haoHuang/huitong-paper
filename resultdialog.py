# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultdialog.ui'
#
# Created: Tue Jul 14 21:18:37 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_ResultDialog(object):
    def setupUi(self, ResultDialog):
        ResultDialog.setObjectName(_fromUtf8("ResultDialog"))
        ResultDialog.resize(235, 137)
        self.resultbuttonBox = QtGui.QDialogButtonBox(ResultDialog)
        self.resultbuttonBox.setGeometry(QtCore.QRect(80, 70, 81, 32))
        self.resultbuttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.resultbuttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.resultbuttonBox.setObjectName(_fromUtf8("resultbuttonBox"))
        self.resultlabel = QtGui.QLabel(ResultDialog)
        self.resultlabel.setGeometry(QtCore.QRect(110, 20, 31, 51))
        self.resultlabel.setObjectName(_fromUtf8("resultlabel"))

        self.retranslateUi(ResultDialog)
        QtCore.QObject.connect(self.resultbuttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ResultDialog.accept)
        QtCore.QObject.connect(self.resultbuttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ResultDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ResultDialog)

    def retranslateUi(self, ResultDialog):
        ResultDialog.setWindowTitle(_translate("ResultDialog", "Dialog", None))
        self.resultlabel.setText(_translate("ResultDialog", "成功", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ResultDialog = QtGui.QDialog()
    ui = Ui_ResultDialog()
    ui.setupUi(ResultDialog)
    ResultDialog.show()
    sys.exit(app.exec_())

