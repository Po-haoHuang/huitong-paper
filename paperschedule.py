# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paperschedule.ui'
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

class Ui_PaperScheduleDialog(object):
    def setupUi(self, PaperScheduleDialog):
        PaperScheduleDialog.setObjectName(_fromUtf8("PaperScheduleDialog"))
        PaperScheduleDialog.resize(415, 309)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PaperScheduleDialog.sizePolicy().hasHeightForWidth())
        PaperScheduleDialog.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(PaperScheduleDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.paperRollNumber = QtGui.QLabel(PaperScheduleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paperRollNumber.sizePolicy().hasHeightForWidth())
        self.paperRollNumber.setSizePolicy(sizePolicy)
        self.paperRollNumber.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.paperRollNumber.setObjectName(_fromUtf8("paperRollNumber"))
        self.gridLayout.addWidget(self.paperRollNumber, 2, 0, 1, 1)
        self.paperWidth = QtGui.QLabel(PaperScheduleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paperWidth.sizePolicy().hasHeightForWidth())
        self.paperWidth.setSizePolicy(sizePolicy)
        self.paperWidth.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.paperWidth.setObjectName(_fromUtf8("paperWidth"))
        self.gridLayout.addWidget(self.paperWidth, 3, 0, 1, 1)
        self.paperScheduleTitle = QtGui.QLabel(PaperScheduleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paperScheduleTitle.sizePolicy().hasHeightForWidth())
        self.paperScheduleTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.paperScheduleTitle.setFont(font)
        self.paperScheduleTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.paperScheduleTitle.setObjectName(_fromUtf8("paperScheduleTitle"))
        self.gridLayout.addWidget(self.paperScheduleTitle, 0, 0, 1, 1)
        self.paperScheduleNotice = QtGui.QLabel(PaperScheduleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paperScheduleNotice.sizePolicy().hasHeightForWidth())
        self.paperScheduleNotice.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.paperScheduleNotice.setFont(font)
        self.paperScheduleNotice.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.paperScheduleNotice.setObjectName(_fromUtf8("paperScheduleNotice"))
        self.gridLayout.addWidget(self.paperScheduleNotice, 1, 0, 1, 5)
        self.paperCustomer = QtGui.QLabel(PaperScheduleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paperCustomer.sizePolicy().hasHeightForWidth())
        self.paperCustomer.setSizePolicy(sizePolicy)
        self.paperCustomer.setObjectName(_fromUtf8("paperCustomer"))
        self.gridLayout.addWidget(self.paperCustomer, 4, 0, 1, 1)
        self.paperPlus = QtGui.QPushButton(PaperScheduleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paperPlus.sizePolicy().hasHeightForWidth())
        self.paperPlus.setSizePolicy(sizePolicy)
        self.paperPlus.setObjectName(_fromUtf8("paperPlus"))
        self.gridLayout.addWidget(self.paperPlus, 0, 1, 1, 1)
        self.paperRollNumberEdit = QtGui.QLineEdit(PaperScheduleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paperRollNumberEdit.sizePolicy().hasHeightForWidth())
        self.paperRollNumberEdit.setSizePolicy(sizePolicy)
        self.paperRollNumberEdit.setObjectName(_fromUtf8("paperRollNumberEdit"))
        self.gridLayout.addWidget(self.paperRollNumberEdit, 2, 1, 1, 1)
        self.paperInputButtonBox = QtGui.QDialogButtonBox(PaperScheduleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paperInputButtonBox.sizePolicy().hasHeightForWidth())
        self.paperInputButtonBox.setSizePolicy(sizePolicy)
        self.paperInputButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.paperInputButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.paperInputButtonBox.setObjectName(_fromUtf8("paperInputButtonBox"))
        self.gridLayout.addWidget(self.paperInputButtonBox, 5, 0, 1, 1)

        self.retranslateUi(PaperScheduleDialog)
        QtCore.QObject.connect(self.paperInputButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PaperScheduleDialog.accept)
        QtCore.QObject.connect(self.paperInputButtonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PaperScheduleDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PaperScheduleDialog)

    def retranslateUi(self, PaperScheduleDialog):
        PaperScheduleDialog.setWindowTitle(_translate("PaperScheduleDialog", "正規紙排單", None))
        self.paperRollNumber.setText(_translate("PaperScheduleDialog", "<html><head/><body><p>顆數:</p></body></html>", None))
        self.paperWidth.setText(_translate("PaperScheduleDialog", "<html><head/><body><p>紙幅(mm):</p></body></html>", None))
        self.paperScheduleTitle.setText(_translate("PaperScheduleDialog", "正規紙排單", None))
        self.paperScheduleNotice.setText(_translate("PaperScheduleDialog", "請輸入排單使用量", None))
        self.paperCustomer.setText(_translate("PaperScheduleDialog", "客戶", None))
        self.paperPlus.setText(_translate("PaperScheduleDialog", "+", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PaperScheduleDialog = QtGui.QDialog()
    ui = Ui_PaperScheduleDialog()
    ui.setupUi(PaperScheduleDialog)
    PaperScheduleDialog.show()
    sys.exit(app.exec_())

