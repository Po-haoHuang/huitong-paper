# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultdialog.ui'
#
# Created: Tue Jul 21 16:48:26 2015
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
        self.verticalLayout = QtGui.QVBoxLayout(ResultDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.resultlabel = QtGui.QLabel(ResultDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultlabel.sizePolicy().hasHeightForWidth())
        self.resultlabel.setSizePolicy(sizePolicy)
        self.resultlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultlabel.setObjectName(_fromUtf8("resultlabel"))
        self.verticalLayout.addWidget(self.resultlabel, QtCore.Qt.AlignHCenter)
        self.resultbuttonBox = QtGui.QDialogButtonBox(ResultDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultbuttonBox.sizePolicy().hasHeightForWidth())
        self.resultbuttonBox.setSizePolicy(sizePolicy)
        self.resultbuttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.resultbuttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.resultbuttonBox.setCenterButtons(False)
        self.resultbuttonBox.setObjectName(_fromUtf8("resultbuttonBox"))
        self.verticalLayout.addWidget(self.resultbuttonBox, QtCore.Qt.AlignHCenter)

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

