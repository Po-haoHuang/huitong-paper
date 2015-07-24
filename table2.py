# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Jul 21 15:36:01 2015
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(855, 635)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.paperInputTitle = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.paperInputTitle.setFont(font)
        self.paperInputTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.paperInputTitle.setObjectName(_fromUtf8("paperInputTitle"))
        self.verticalLayout.addWidget(self.paperInputTitle)
        self.systemStatusComboBox = QtGui.QComboBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.systemStatusComboBox.sizePolicy().hasHeightForWidth())
        self.systemStatusComboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.systemStatusComboBox.setFont(font)
        self.systemStatusComboBox.setObjectName(_fromUtf8("systemStatusComboBox"))
        self.systemStatusComboBox.addItem(_fromUtf8(""))
        self.systemStatusComboBox.addItem(_fromUtf8(""))
        self.systemStatusComboBox.addItem(_fromUtf8(""))
        self.systemStatusComboBox.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.systemStatusComboBox)
        self.tableView = QtGui.QTableView(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableView.setFont(font)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout.addWidget(self.tableView)
        self.paperInputPushButton = QtGui.QPushButton(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.paperInputPushButton.setFont(font)
        self.paperInputPushButton.setCheckable(False)
        self.paperInputPushButton.setChecked(False)
        self.paperInputPushButton.setObjectName(_fromUtf8("paperInputPushButton"))
        self.verticalLayout.addWidget(self.paperInputPushButton)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.systemStatusComboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.paperInputTitle.setText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "正規紙庫存系統", None))
        self.paperInputTitle.setText(_translate("MainWindow", "到港未入庫", None))
        self.systemStatusComboBox.setItemText(0, _translate("MainWindow", "到港未入庫", None))
        self.systemStatusComboBox.setItemText(1, _translate("MainWindow", "正規紙庫存", None))
        self.systemStatusComboBox.setItemText(2, _translate("MainWindow", "正規紙排單", None))
        self.systemStatusComboBox.setItemText(3, _translate("MainWindow", "排單剩餘", None))
        self.paperInputPushButton.setText(_translate("MainWindow", "輸入", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

