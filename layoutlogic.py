# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 23:23:41 2015

@author: Paul
"""

from PyQt4 import QtCore, QtGui, QtSql, Qt
import os
import database
import paperinputdialog
import table2
import resultdialog

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

nameList = ["批號","紙幅(mm)","顆數","規格(基重條數)","重量(kg)","原基重(gsm)","狀態","米數(m)"]

def DBSetup():
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(os.getcwdu()+os.sep+'papers.sqlite')
    db.open()
    #print db.tables()
    return db
#   db.setDatabaseName("D:\\huitong-paper\\papers.sqlite")
def SQLModelSetup(db,status):
    model = QtSql.QSqlTableModel(None,db)
    model.setTable("paper")
    model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
    model.setFilter('paper_status = ' + str(status))
    model.select()
    for i in range(model.columnCount()):
        model.setHeaderData(i,Qt.Qt.Horizontal, _translate("model",nameList[i],None))
    return model
#    model = QtSql.QSqlQueryModel()
#    model.setQuery("SELECT * FROM paper".encode('utf8'))
#    print model.lastError().text()
#    model.setHeaderData(0,1, "paperWeight")
def TableViewSetup(ui, model):
    ui.tableView.setModel(model)
    ui.tableView.hideColumn(6)
    ui.tableView.setSortingEnabled(True)
    ui.tableView.show()

def on_combox_status(model,n):
    model.setFilter('paper_status = ' + str(n))
    model.select()

def on_inputbutton_push(PaperInputDialog):
    PaperInputDialog.exec_()
#    for i in range(model.columnCount()):
#        model.setHeaderData(i,Qt.Qt.Horizontal, _translate("model",nameList[i],None))
#    ui.tableView.setModel(model)
#    ui.tableView.hideColumn(6)
#    ui.tableView.show()

def on_inputpaper_send(ui, paperinputui, model):
    ResultDialog = QtGui.QDialog()
    resultui = resultdialog.Ui_ResultDialog()
    resultui.setupUi(ResultDialog)
    print paperinputui.paperSpecEdit.text()
    try:
        database.InputPaper(paperinputui.groupNumberEdit.text(),\
            paperinputui.paperWidthEdit.text(), paperinputui.paperRollNumberEdit.text(),\
            paperinputui.paperSpecEdit.text(), paperinputui.paperWeightEdit.text(),\
            paperinputui.paperWeighPerUnitEdit.text(), paperinputui.paperLengthEdit.text(),\
            str(ui.systemStatusComboBox.currentIndex()+1))
        resultui.resultlabel.setText(_translate("resultui", "成功", None))
    except Exception,e:
        print e
        resultui.resultlabel.setText(_translate("resultui", "失敗，請檢查輸入", None))
    model.select()
    ResultDialog.exec_()

def LayoutLogicSetup(ui,status):
    db = DBSetup()
    model = SQLModelSetup(db, ui.systemStatusComboBox.currentIndex()+1)
    TableViewSetup(ui, model)
    PaperInputDialog = QtGui.QDialog()
    paperinputui = paperinputdialog.Ui_PaperInputDialog()
    paperinputui.setupUi(PaperInputDialog)
    ui.systemStatusComboBox.currentIndexChanged.connect(lambda: on_combox_status(model, ui.systemStatusComboBox.currentIndex()+1))
    ui.paperInputPushButton.clicked.connect(lambda: on_inputbutton_push(PaperInputDialog))
    #print paperinputui.groupNumberEdit.text()
    #print type(paperinputui.groupNumberEdit.text())
    paperinputui.paperInputButtonBox.accepted.connect(lambda: on_inputpaper_send(ui, paperinputui, model))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = table2.Ui_MainWindow()
    ui.setupUi(MainWindow)
    LayoutLogicSetup(ui, ui.systemStatusComboBox.currentIndex()+1)
    MainWindow.show()
    sys.exit(app.exec_())
#    import sys
#    app = QtGui.QApplication(sys.argv)
#    MainWindow = QtGui.QMainWindow()
#    ui = table2.Ui_MainWindow()
#    ui.setupUi(MainWindow)
##    DB = DBSetup()
##    Model = SQLModelSetup(ui.systemStatusComboBox.currentIndex()+1)
##    TableViewSetup(ui)
#    LayoutLogicSetup(ui,1)
#    #ui.systemStatusComboBox.currentIndexChanged.connect(lambda: on_combox_status(ui.systemStatusComboBox.currentIndex()+1))
##    ui.paperInputPushButton.clicked.connect(lambda: on_inputbutton_push())
##    PaperInputDialog = QtGui.QDialog()
##    paperinputui = paperinputdialog.Ui_PaperInputDialog()
##    paperinputui.setupUi(PaperInputDialog)
##    print paperinputui.groupNumberEdit.text()
##    print type(paperinputui.groupNumberEdit.text())
##    paperinputui.paperInputButtonBox.accepted.connect(lambda: database.InputPaper(paperinputui.groupNumberEdit.text(),\
##        paperinputui.paperWidthEdit.text(), paperinputui.paperRollNumberEdit.text(),\
##        paperinputui.paperSpecEdit.text(), paperinputui.paperWeightEdit.text(),\
##        paperinputui.paperWeighPerUnitEdit.text(), paperinputui.paperLengthEdit.text(),\
##        ui.systemStatusComboBox.currentIndex()+1))
#    MainWindow.show()
#    sys.exit(app.exec_())


#    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
#    db.setDatabaseName(os.getcwdu()+os.sep+'papers.sqlite')
#    #db.setDatabaseName("D:\\huitong-paper\\papers.sqlite")
#    print db.open()
#    print db.tables()
#    model = QtSql.QSqlTableModel(None,db)
#    model.setTable("paper");
#    model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit);
#    model.select();
##    model = QtSql.QSqlQueryModel()
##    model.setQuery("SELECT * FROM paper".encode('utf8'))
#    #print model.lastError().text()
##    model.setHeaderData(0,1, "paperWeight")
#    ui.tableView.setModel(model)
#    ui.tableView.show()
#    ui.tableView.setSortingEnabled(True)
