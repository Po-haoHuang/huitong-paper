# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Jul 07 00:33:15 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import layoutlogic

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1000, 420)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 420))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 420))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.FS_inputLable = QtGui.QLabel(self.centralWidget)
        self.FS_inputLable.setGeometry(QtCore.QRect(490, 40, 71, 51))
        self.FS_inputLable.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FS_inputLable.setObjectName(_fromUtf8("FS_inputLable"))
        self.FS_InputFileLabel = QtGui.QLabel(self.centralWidget)
        self.FS_InputFileLabel.setGeometry(QtCore.QRect(600, 80, 351, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FS_InputFileLabel.sizePolicy().hasHeightForWidth())
        self.FS_InputFileLabel.setSizePolicy(sizePolicy)
        self.FS_InputFileLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FS_InputFileLabel.setObjectName(_fromUtf8("FS_InputFileLabel"))
        self.FS_ChooseFile = QtGui.QPushButton(self.centralWidget)
        self.FS_ChooseFile.setGeometry(QtCore.QRect(590, 50, 93, 28))
        self.FS_ChooseFile.setCheckable(False)
        self.FS_ChooseFile.setChecked(False)
        self.FS_ChooseFile.setObjectName(_fromUtf8("FS_ChooseFile"))
        self.FS_FeaturnameBox = QtGui.QComboBox(self.centralWidget)
        self.FS_FeaturnameBox.setGeometry(QtCore.QRect(590, 110, 341, 22))
        self.FS_FeaturnameBox.setObjectName(_fromUtf8("FS_FeaturnameBox"))
        self.label_6 = QtGui.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(490, 100, 101, 41))
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(490, 130, 111, 41))
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.FS_DMethodBox = QtGui.QComboBox(self.centralWidget)
        self.FS_DMethodBox.setEnabled(True)
        self.FS_DMethodBox.setGeometry(QtCore.QRect(590, 140, 131, 22))
        self.FS_DMethodBox.setObjectName(_fromUtf8("FS_DMethodBox"))
        self.FS_DMethodBox.addItem(_fromUtf8(""))
        self.FS_DMethodBox.addItem(_fromUtf8(""))
        self.label_8 = QtGui.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(740, 250, 161, 21))
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(490, 250, 111, 21))
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralWidget)
        self.label_10.setGeometry(QtCore.QRect(490, 280, 121, 21))
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.centralWidget)
        self.label_11.setGeometry(QtCore.QRect(490, 310, 121, 21))
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(870, 360, 91, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_12 = QtGui.QLabel(self.centralWidget)
        self.label_12.setEnabled(True)
        self.label_12.setGeometry(QtCore.QRect(780, 130, 131, 41))
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.lineEdit_5 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_5.setGeometry(QtCore.QRect(890, 140, 61, 22))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_13 = QtGui.QLabel(self.centralWidget)
        self.label_13.setGeometry(QtCore.QRect(490, 220, 111, 21))
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_7 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(890, 220, 61, 21))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.label_14 = QtGui.QLabel(self.centralWidget)
        self.label_14.setGeometry(QtCore.QRect(740, 220, 111, 21))
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 60, 111, 28))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 51, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_4 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 360, 91, 31))
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.paperInputTitle = QtGui.QLabel(self.centralWidget)
        self.paperInputTitle.setGeometry(QtCore.QRect(10, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.paperInputTitle.setFont(font)
        self.paperInputTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.paperInputTitle.setObjectName(_fromUtf8("paperInputTitle"))
        self.label_19 = QtGui.QLabel(self.centralWidget)
        self.label_19.setGeometry(QtCore.QRect(480, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.line = QtGui.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(440, 10, 20, 401))
        self.line.setMaximumSize(QtCore.QSize(16777215, 16777214))
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.comboBox = QtGui.QComboBox(self.centralWidget)
        self.comboBox.setGeometry(QtCore.QRect(590, 220, 51, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox_2 = QtGui.QComboBox(self.centralWidget)
        self.comboBox_2.setGeometry(QtCore.QRect(590, 250, 51, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_3 = QtGui.QComboBox(self.centralWidget)
        self.comboBox_3.setGeometry(QtCore.QRect(590, 280, 51, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_4 = QtGui.QComboBox(self.centralWidget)
        self.comboBox_4.setGeometry(QtCore.QRect(590, 310, 51, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_6 = QtGui.QComboBox(self.centralWidget)
        self.comboBox_6.setGeometry(QtCore.QRect(890, 250, 61, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_6.sizePolicy().hasHeightForWidth())
        self.comboBox_6.setSizePolicy(sizePolicy)
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.label_17 = QtGui.QLabel(self.centralWidget)
        self.label_17.setGeometry(QtCore.QRect(740, 310, 111, 21))
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.comboBox_7 = QtGui.QComboBox(self.centralWidget)
        self.comboBox_7.setGeometry(QtCore.QRect(890, 310, 61, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_7.sizePolicy().hasHeightForWidth())
        self.comboBox_7.setSizePolicy(sizePolicy)
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.line_2 = QtGui.QFrame(self.centralWidget)
        self.line_2.setGeometry(QtCore.QRect(460, 170, 531, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_20 = QtGui.QLabel(self.centralWidget)
        self.label_20.setGeometry(QtCore.QRect(480, 180, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.centralWidget)
        self.label_21.setGeometry(QtCore.QRect(740, 280, 111, 21))
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.lineEdit_10 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(890, 280, 61, 22))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.pushButton_5 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(520, 360, 121, 31))
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(690, 360, 131, 31))
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.comboBox_5 = QtGui.QComboBox(self.centralWidget)
        self.comboBox_5.setGeometry(QtCore.QRect(340, 20, 81, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.tableView = QtGui.QTableView(self.centralWidget)
        self.tableView.setGeometry(QtCore.QRect(30, 100, 401, 241))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Feature_Selection System", None))
        self.FS_inputLable.setText(_translate("MainWindow", "<html><head/><body><p>Input File:</p></body></html>", None))
        self.FS_InputFileLabel.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.FS_ChooseFile.setText(_translate("MainWindow", "Choose File", None))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>Target Feature:</p></body></html>", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>Discretize Method:</p></body></html>", None))
        self.FS_DMethodBox.setItemText(0, _translate("MainWindow", "Equal Weight(Cycle)", None))
        self.FS_DMethodBox.setItemText(1, _translate("MainWindow", "Manual", None))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>Top N Feature(For Output):</p></body></html>", None))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p>Lasso (λ):</p></body></html>", None))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p>Elastic Net (λ<span style=\" vertical-align:sub;\">1</span>):</p></body></html>", None))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p>Elastic Net (λ<span style=\" vertical-align:sub;\">2</span>):</p></body></html>", None))
        self.pushButton.setText(_translate("MainWindow", "Start", None))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p>EW_Cycle Number:</p></body></html>", None))
        self.lineEdit_5.setText(_translate("MainWindow", "3", None))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p>Ridge (λ):</p></body></html>", None))
        self.lineEdit_7.setText(_translate("MainWindow", "0.01", None))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p>FCBF Threshold:</p></body></html>", None))
        self.pushButton_2.setText(_translate("MainWindow", "Choose File", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>檔案匯入:</p></body></html>", None))
        self.pushButton_4.setText(_translate("MainWindow", "輸入", None))
        self.paperInputTitle.setText(_translate("MainWindow", "<html><head/><body><p>正規紙庫存</p></body></html>", None))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p>排單剩餘</p></body></html>", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "1", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "2", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "3", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "2", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "3", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "1", None))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "2", None))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "3", None))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "1", None))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "2", None))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "3", None))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "1", None))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "2", None))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "3", None))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "4", None))
        self.comboBox_6.setItemText(4, _translate("MainWindow", "5", None))
        self.comboBox_6.setItemText(5, _translate("MainWindow", "6", None))
        self.comboBox_6.setItemText(6, _translate("MainWindow", "7", None))
        self.comboBox_6.setItemText(7, _translate("MainWindow", "8", None))
        self.comboBox_6.setItemText(8, _translate("MainWindow", "9", None))
        self.comboBox_6.setItemText(9, _translate("MainWindow", "10", None))
        self.comboBox_6.setItemText(10, _translate("MainWindow", "11", None))
        self.comboBox_6.setItemText(11, _translate("MainWindow", "12", None))
        self.comboBox_6.setItemText(12, _translate("MainWindow", "13", None))
        self.comboBox_6.setItemText(13, _translate("MainWindow", "14", None))
        self.comboBox_6.setItemText(14, _translate("MainWindow", "15", None))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p>Discretize by cycle:</p></body></html>", None))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "False", None))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "True", None))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#7f7f7f;\">Algorithm Parameters</span></p></body></html>", None))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p>Top K(For MI):</p></body></html>", None))
        self.lineEdit_10.setText(_translate("MainWindow", "20", None))
        self.pushButton_5.setText(_translate("MainWindow", "Edit Exclude Feature", None))
        self.pushButton_6.setText(_translate("MainWindow", "Edit Include Feature", None))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "到港未入庫", None))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "正規紙庫存", None))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "正規紙排單", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    layoutlogic.LayoutLogicSetup(ui)
    MainWindow.show()
    sys.exit(app.exec_())

