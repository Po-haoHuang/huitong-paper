# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 23:23:41 2015

@author: Paul
"""

from PyQt4 import QtCore, QtGui, QtSql
import os

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
        
def DBSetup():
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(os.getcwdu()+os.sep+'papers.sqlite')
    print db.open()
    print db.tables()
    return db
#db.setDatabaseName("D:\\huitong-paper\\papers.sqlite")
def SQLModelSetup(db):
	model = QtSql.QSqlTableModel(None,db)
	model.setTable("paper")
	model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
	model.select()
	return model
#    model = QtSql.QSqlQueryModel()
#    model.setQuery("SELECT * FROM paper".encode('utf8'))
    #print model.lastError().text()
#    model.setHeaderData(0,1, "paperWeight")
def TableViewSetuo(ui,model):
	ui.tableView.setModel(model)
	ui.tableView.show()
	ui.tableView.setSortingEnabled(True)

