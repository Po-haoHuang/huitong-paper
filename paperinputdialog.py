# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paperinput.ui'
#
# Created: Tue Jul 14 17:24:37 2015
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

class Ui_PaperInputDialog(object):
    def setupUi(self, PaperInputDialog):
        PaperInputDialog.setObjectName(_fromUtf8("PaperInputDialog"))
        PaperInputDialog.resize(436, 324)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PaperInputDialog.sizePolicy().hasHeightForWidth())
        PaperInputDialog.setSizePolicy(sizePolicy)
        PaperInputDialog.setMaximumSize(QtCore.QSize(436, 324))
        self.paperInputButtonBox = QtGui.QDialogButtonBox(PaperInputDialog)
        self.paperInputButtonBox.setGeometry(QtCore.QRect(130, 250, 161, 32))
        self.paperInputButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.paperInputButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.paperInputButtonBox.setObjectName(_fromUtf8("paperInputButtonBox"))
        self.paperLength = QtGui.QLabel(PaperInputDialog)
        self.paperLength.setGeometry(QtCore.QRect(280, 90, 51, 31))
        self.paperLength.setObjectName(_fromUtf8("paperLength"))
        self.groupNumber = QtGui.QLabel(PaperInputDialog)
        self.groupNumber.setGeometry(QtCore.QRect(10, 52, 31, 41))
        self.groupNumber.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupNumber.setObjectName(_fromUtf8("groupNumber"))
        self.paperWeightEdit = QtGui.QLineEdit(PaperInputDialog)
        self.paperWeightEdit.setGeometry(QtCore.QRect(70, 92, 61, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paperWeightEdit.sizePolicy().hasHeightForWidth())
        self.paperWeightEdit.setSizePolicy(sizePolicy)
        self.paperWeightEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.paperWeightEdit.setMaximumSize(QtCore.QSize(110, 16777215))
        self.paperWeightEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.paperWeightEdit.setInputMask(_fromUtf8(""))
        self.paperWeightEdit.setText(_fromUtf8(""))
        self.paperWeightEdit.setMaxLength(32767)
        self.paperWeightEdit.setCursorPosition(0)
        self.paperWeightEdit.setDragEnabled(False)
        self.paperWeightEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.paperWeightEdit.setProperty("clearButtonEnabled", False)
        self.paperWeightEdit.setObjectName(_fromUtf8("paperWeightEdit"))
        self.paperWeighPerUnit = QtGui.QLabel(PaperInputDialog)
        self.paperWeighPerUnit.setGeometry(QtCore.QRect(140, 90, 71, 31))
        self.paperWeighPerUnit.setObjectName(_fromUtf8("paperWeighPerUnit"))
        self.paperRollNumber = QtGui.QLabel(PaperInputDialog)
        self.paperRollNumber.setGeometry(QtCore.QRect(280, 50, 31, 41))
        self.paperRollNumber.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.paperRollNumber.setObjectName(_fromUtf8("paperRollNumber"))
        self.paperLengthEdit = QtGui.QLineEdit(PaperInputDialog)
        self.paperLengthEdit.setGeometry(QtCore.QRect(340, 90, 61, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paperLengthEdit.sizePolicy().hasHeightForWidth())
        self.paperLengthEdit.setSizePolicy(sizePolicy)
        self.paperLengthEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.paperLengthEdit.setMaximumSize(QtCore.QSize(110, 16777215))
        self.paperLengthEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.paperLengthEdit.setInputMask(_fromUtf8(""))
        self.paperLengthEdit.setText(_fromUtf8(""))
        self.paperLengthEdit.setMaxLength(32767)
        self.paperLengthEdit.setCursorPosition(0)
        self.paperLengthEdit.setDragEnabled(False)
        self.paperLengthEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.paperLengthEdit.setProperty("clearButtonEnabled", False)
        self.paperLengthEdit.setObjectName(_fromUtf8("paperLengthEdit"))
        self.paperSpecEdit = QtGui.QLineEdit(PaperInputDialog)
        self.paperSpecEdit.setGeometry(QtCore.QRect(100, 122, 61, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paperSpecEdit.sizePolicy().hasHeightForWidth())
        self.paperSpecEdit.setSizePolicy(sizePolicy)
        self.paperSpecEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.paperSpecEdit.setMaximumSize(QtCore.QSize(110, 16777215))
        self.paperSpecEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.paperSpecEdit.setInputMask(_fromUtf8(""))
        self.paperSpecEdit.setText(_fromUtf8(""))
        self.paperSpecEdit.setMaxLength(32767)
        self.paperSpecEdit.setCursorPosition(0)
        self.paperSpecEdit.setDragEnabled(False)
        self.paperSpecEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.paperSpecEdit.setProperty("clearButtonEnabled", False)
        self.paperSpecEdit.setObjectName(_fromUtf8("paperSpecEdit"))
        self.paperInputTitle = QtGui.QLabel(PaperInputDialog)
        self.paperInputTitle.setGeometry(QtCore.QRect(10, 12, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.paperInputTitle.setFont(font)
        self.paperInputTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.paperInputTitle.setObjectName(_fromUtf8("paperInputTitle"))
        self.paperSpec = QtGui.QLabel(PaperInputDialog)
        self.paperSpec.setGeometry(QtCore.QRect(10, 122, 91, 31))
        self.paperSpec.setObjectName(_fromUtf8("paperSpec"))
        self.paperWeighPerUnitEdit = QtGui.QLineEdit(PaperInputDialog)
        self.paperWeighPerUnitEdit.setGeometry(QtCore.QRect(210, 90, 61, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paperWeighPerUnitEdit.sizePolicy().hasHeightForWidth())
        self.paperWeighPerUnitEdit.setSizePolicy(sizePolicy)
        self.paperWeighPerUnitEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.paperWeighPerUnitEdit.setMaximumSize(QtCore.QSize(110, 16777215))
        self.paperWeighPerUnitEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.paperWeighPerUnitEdit.setInputMask(_fromUtf8(""))
        self.paperWeighPerUnitEdit.setText(_fromUtf8(""))
        self.paperWeighPerUnitEdit.setMaxLength(32767)
        self.paperWeighPerUnitEdit.setCursorPosition(0)
        self.paperWeighPerUnitEdit.setDragEnabled(False)
        self.paperWeighPerUnitEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.paperWeighPerUnitEdit.setProperty("clearButtonEnabled", False)
        self.paperWeighPerUnitEdit.setObjectName(_fromUtf8("paperWeighPerUnitEdit"))
        self.paperWeight = QtGui.QLabel(PaperInputDialog)
        self.paperWeight.setGeometry(QtCore.QRect(10, 92, 51, 31))
        self.paperWeight.setObjectName(_fromUtf8("paperWeight"))
        self.groupNumberEdit = QtGui.QLineEdit(PaperInputDialog)
        self.groupNumberEdit.setGeometry(QtCore.QRect(70, 64, 61, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupNumberEdit.sizePolicy().hasHeightForWidth())
        self.groupNumberEdit.setSizePolicy(sizePolicy)
        self.groupNumberEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.groupNumberEdit.setMaximumSize(QtCore.QSize(110, 16777215))
        self.groupNumberEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.groupNumberEdit.setInputMask(_fromUtf8(""))
        self.groupNumberEdit.setText(_fromUtf8(""))
        self.groupNumberEdit.setMaxLength(32767)
        self.groupNumberEdit.setCursorPosition(0)
        self.groupNumberEdit.setDragEnabled(False)
        self.groupNumberEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.groupNumberEdit.setProperty("clearButtonEnabled", False)
        self.groupNumberEdit.setObjectName(_fromUtf8("groupNumberEdit"))
        self.paperWidthEdit = QtGui.QLineEdit(PaperInputDialog)
        self.paperWidthEdit.setGeometry(QtCore.QRect(210, 62, 61, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paperWidthEdit.sizePolicy().hasHeightForWidth())
        self.paperWidthEdit.setSizePolicy(sizePolicy)
        self.paperWidthEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.paperWidthEdit.setMaximumSize(QtCore.QSize(110, 16777215))
        self.paperWidthEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.paperWidthEdit.setInputMask(_fromUtf8(""))
        self.paperWidthEdit.setText(_fromUtf8(""))
        self.paperWidthEdit.setMaxLength(32767)
        self.paperWidthEdit.setCursorPosition(0)
        self.paperWidthEdit.setDragEnabled(False)
        self.paperWidthEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.paperWidthEdit.setProperty("clearButtonEnabled", False)
        self.paperWidthEdit.setObjectName(_fromUtf8("paperWidthEdit"))
        self.paperRollNumberEdit = QtGui.QLineEdit(PaperInputDialog)
        self.paperRollNumberEdit.setGeometry(QtCore.QRect(340, 62, 61, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paperRollNumberEdit.sizePolicy().hasHeightForWidth())
        self.paperRollNumberEdit.setSizePolicy(sizePolicy)
        self.paperRollNumberEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.paperRollNumberEdit.setMaximumSize(QtCore.QSize(110, 16777215))
        self.paperRollNumberEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.paperRollNumberEdit.setInputMask(_fromUtf8(""))
        self.paperRollNumberEdit.setText(_fromUtf8(""))
        self.paperRollNumberEdit.setMaxLength(32767)
        self.paperRollNumberEdit.setCursorPosition(0)
        self.paperRollNumberEdit.setDragEnabled(False)
        self.paperRollNumberEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.paperRollNumberEdit.setProperty("clearButtonEnabled", False)
        self.paperRollNumberEdit.setObjectName(_fromUtf8("paperRollNumberEdit"))
        self.paperWidth = QtGui.QLabel(PaperInputDialog)
        self.paperWidth.setGeometry(QtCore.QRect(140, 50, 61, 41))
        self.paperWidth.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.paperWidth.setObjectName(_fromUtf8("paperWidth"))

        self.retranslateUi(PaperInputDialog)
        QtCore.QObject.connect(self.paperInputButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PaperInputDialog.accept)
        QtCore.QObject.connect(self.paperInputButtonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PaperInputDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PaperInputDialog)

    def retranslateUi(self, PaperInputDialog):
        PaperInputDialog.setWindowTitle(_translate("PaperInputDialog", "正規紙入庫", None))
        self.paperLength.setText(_translate("PaperInputDialog", "米數(m):", None))
        self.groupNumber.setText(_translate("PaperInputDialog", "<html><head/><body><p>批號:</p></body></html>", None))
        self.paperWeighPerUnit.setText(_translate("PaperInputDialog", "原基重(gsm):", None))
        self.paperRollNumber.setText(_translate("PaperInputDialog", "<html><head/><body><p>顆數:</p></body></html>", None))
        self.paperInputTitle.setText(_translate("PaperInputDialog", "<html><head/><body><p>正規紙入庫</p></body></html>", None))
        self.paperSpec.setText(_translate("PaperInputDialog", "規格(基重條數):", None))
        self.paperWeight.setText(_translate("PaperInputDialog", "重量(kg):", None))
        self.paperWidth.setText(_translate("PaperInputDialog", "<html><head/><body><p>紙幅(mm):</p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PaperInputDialog = QtGui.QDialog()
    ui = Ui_PaperInputDialog()
    ui.setupUi(PaperInputDialog)
    PaperInputDialog.show()
    sys.exit(app.exec_())
