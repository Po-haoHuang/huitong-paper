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
import modifydialog
import paperschedule

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


class mySqlTableModel(QtSql.QSqlTableModel):
    currentSelectedIndex = 0
    def data(self, index, role):
        if index.isValid():
            if role == QtCore.Qt.BackgroundRole and self.record(index.row()).value('paper_status') >= 5 :
                return QtGui.QBrush(QtCore.Qt.gray)
            elif role == QtCore.Qt.FontRole and self.record(index.row()).value('paper_status') >= 5 :
                font = QtGui.QFont()
                font.setBold(True)
                return font
            else:
                return QtSql.QSqlTableModel.data(self,index, role)


nameList = ["批號","紙幅(mm)","原基重(gsm)","規格(基重條數)","顆數","廠商","狀態","米數(m)","重量(kg)"]

def DBSetup():
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(os.getcwd()+os.sep+'papers.sqlite')
    db.open()
    return db

def SQLModelSetup(db,status):
    model = mySqlTableModel(MainWindow,db)
    model.setTable("paper")
    model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
    model.setFilter('paper_status = ' + str(status))
    model.select()
    for i in range(model.columnCount()):
        model.setHeaderData(i,Qt.Qt.Horizontal, _translate("model",nameList[i],None))
    return model


def TableViewSetup(ui, model):
    ui.tableView.setModel(model)
    ui.tableView.hideColumn(6)
    ui.tableView.hideColumn(7)
    ui.tableView.hideColumn(8)    
    ui.tableView.setSortingEnabled(True)
    ui.tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
    ui.tableView.horizontalHeader().setResizeMode(Qt.QHeaderView.Stretch)
    ui.tableView.show()


def on_combox_status(model,n):
    if n == 3 or n == 4:
        model.setFilter('paper_status = ' + str(n) + ' OR paper_status = ' + str(n+2))
        model.select()
    else:
        model.setFilter('paper_status = ' + str(n))
        model.select()
    if n == 1:
        ui.paperInputPushButton.setDisabled(False)
        ui.paperInputPushButton.setVisible(True)
        ui.paperInputPushButton.setText(_translate("paperInputPushButton", "輸入", None))
#    elif n == 2:
#        ui.paperInputPushButton.setDisabled(False)
#        ui.paperInputPushButton.setVisible(True)
#        ui.paperInputPushButton.setText(_translate("paperInputPushButton", "排單", None))
    else:
        ui.paperInputPushButton.setDisabled(True)
        ui.paperInputPushButton.setVisible(False)

def on_inputbutton_push():
    if ui.systemStatusComboBox.currentIndex() == 0:
        paperinputui.groupNumberEdit.clear()
        paperinputui.paperRollNumberEdit.clear()
        paperinputui.paperSpecEdit.clear()
        paperinputui.paperWeighPerUnitEdit.clear()
        paperinputui.paperCustomerEdit.clear()
        paperinputui.paperWidthEdit.clear()
        PaperInputDialog.exec_()
    else:
        pass


def on_paperinput_send(ui, paperinputui, model):
#    print paperinputui.paperSpecEdit.text()
    ret = database.InputPaper(paperinputui.groupNumberEdit.text(),\
        paperinputui.paperWidthEdit.text(), paperinputui.paperWeighPerUnitEdit.text(),\
        paperinputui.paperSpecEdit.text(), paperinputui.paperRollNumberEdit.text(),\
        paperinputui.paperCustomerEdit.text(), str(ui.systemStatusComboBox.currentIndex()+1))
    if ret == 0:
        resultui.resultlabel.setText(_translate("resultui", "成功", None))
        #resultui.resultlabel.setAlignment()
        #resultui.resultlabel.adjustSize()
    else:
        resultui.resultlabel.setText(_translate("resultui", "失敗，請檢查輸入", None))
        #resultui.resultlabel.adjustSize()
    model.select()
    ResultDialog.exec_()


def on_tableView_horizontalHeader_sectionClicked(index):
    model.currentSelectedIndex = index
    if model.record(index).value('paper_status') == 1:
        modifyui.transferpushButton.setText(_translate("modifyui", "入庫", None))
    elif model.record(index).value('paper_status') == 2:
        modifyui.transferpushButton.setText(_translate("modifyui", "排單", None))
    elif model.record(index).value('paper_status') == 3:
        modifyui.transferpushButton.setText(_translate("modifyui", "出貨", None))

    elif model.record(index).value('paper_status') == 4:
        modifyui.transferpushButton.setText(_translate("modifyui", "出貨", None))

    elif model.record(index).value('paper_status') == 5:
        modifyui.transferpushButton.setText(_translate("modifyui", "完工", None))

    elif model.record(index).value('paper_status') == 6:
        modifyui.transferpushButton.setText(_translate("modifyui", "完工", None))

    else :
        modifyui.transferpushButton.setDisabled(True)
        modifyui.transferpushButton.setVisible(False)

#    print model.record(index).value(0)
    ModifyDialog.exec_()

def on_modify_send():
    if modifyui.deletecheckBox.isChecked() == True:
        #print model.record(model.currentSelectedIndex).value('paper_spec')
        modifyui.deletecheckBox.setChecked(False)
        model.removeRow(model.currentSelectedIndex)
        model.submitAll()
        return

def on_transfer_push():
    if model.record(model.currentSelectedIndex).value('paper_status') == 1:
        record = QtSql.QSqlRecord(model.record(model.currentSelectedIndex))
        record.setValue('paper_status', 2)
        model.setRecord(model.currentSelectedIndex, record)
    elif model.record(model.currentSelectedIndex).value('paper_status') == 2:
        for i in range(0, 10):
            paperscheduleui.gridLayout.removeWidget(paperscheduleui.paperCustomerEdit[i])
            paperscheduleui.gridLayout.removeWidget(paperscheduleui.paperWidthEdit[i])
            paperscheduleui.paperCustomerEdit[i].setVisible(False)
            paperscheduleui.paperWidthEdit[i].setVisible(False)
        paperscheduleui.editCount = 2       
        for i in range(paperscheduleui.editCount):
            paperscheduleui.gridLayout.addWidget(paperscheduleui.paperWidthEdit[i], 3, i+1, 1, 1)
            paperscheduleui.gridLayout.addWidget(paperscheduleui.paperCustomerEdit[i], 4, i+1, 1, 1)
            paperscheduleui.paperWidthEdit[i].clear()
            paperscheduleui.paperCustomerEdit[i].clear()
            paperscheduleui.paperWidthEdit[i].setVisible(True)
            paperscheduleui.paperCustomerEdit[i].setVisible(True)        
        PaperScheduleDialog.exec_()

    elif model.record(model.currentSelectedIndex).value('paper_status') == 3:
        model.removeRow(model.currentSelectedIndex)
    elif model.record(model.currentSelectedIndex).value('paper_status') == 4:
        model.removeRow(model.currentSelectedIndex)
    elif model.record(model.currentSelectedIndex).value('paper_status') == 5:
        record = QtSql.QSqlRecord(model.record(model.currentSelectedIndex))
        record.setValue('paper_status', 3)
        model.setRecord(model.currentSelectedIndex, record)
    elif model.record(model.currentSelectedIndex).value('paper_status') == 6:
        record = QtSql.QSqlRecord(model.record(model.currentSelectedIndex))
        record.setValue('paper_status', 4)
        model.setRecord(model.currentSelectedIndex, record)
    else :
        pass
    model.submitAll()
    ModifyDialog.close()

def on_paperschedule_plus():
    if paperscheduleui.editCount  < 10:
        i = paperscheduleui.editCount
        paperscheduleui.editCount += 1
        paperscheduleui.gridLayout.addWidget(paperscheduleui.paperWidthEdit[i], 3, i+1, 1, 1)
        paperscheduleui.gridLayout.addWidget(paperscheduleui.paperCustomerEdit[i], 4, i+1, 1, 1)
        paperscheduleui.paperWidthEdit[i].clear()
        paperscheduleui.paperCustomerEdit[i].clear()   
        paperscheduleui.paperWidthEdit[i].setVisible(True)
        paperscheduleui.paperCustomerEdit[i].setVisible(True)
    else:
        pass

def on_paperschedule_send():
    ret = {}
    record = model.record(model.currentSelectedIndex)
    for i in range(0, paperscheduleui.editCount):
        if paperscheduleui.paperCustomerEdit[i].text() == "":            
            ret[i] = database.InputPaper(record.value('group_number'),\
            paperscheduleui.paperWidthEdit[i].text(), record.value('paper_weight_per_unit'),\
            record.value('paper_spec'), paperscheduleui.paperRollNumberEdit.text(),\
            paperscheduleui.paperCustomerEdit[i].text(), 6)
        else:
            ret[i] = database.InputPaper(record.value('group_number'),\
            paperscheduleui.paperWidthEdit[i].text(), record.value('paper_weight_per_unit'),\
            record.value('paper_spec'), paperscheduleui.paperRollNumberEdit.text(),\
            paperscheduleui.paperCustomerEdit[i].text(), 5)            
    
        if ret[i] == 0:
            resultui.resultlabel.setText(_translate("resultui", "成功", None))
        else:
            resultui.resultlabel.setText(_translate("resultui", "失敗，請檢查輸入", None))
            break

    if int(paperscheduleui.paperRollNumberEdit.text()) \
                == model.record(model.currentSelectedIndex).value('paper_roll_number'):
        model.removeRow(model.currentSelectedIndex)
    else:
        record = QtSql.QSqlRecord(model.record(model.currentSelectedIndex))
        record.setValue('paper_roll_number', model.record(model.currentSelectedIndex).value('paper_roll_number') - int(paperscheduleui.paperRollNumberEdit.text()))
        model.setRecord(model.currentSelectedIndex, record)
    model.submitAll()
    ResultDialog.exec_()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = table2.Ui_MainWindow()
    ui.setupUi(MainWindow)
    db = DBSetup()
    model = SQLModelSetup(db, ui.systemStatusComboBox.currentIndex()+1)
    TableViewSetup(ui, model)

    PaperInputDialog = QtGui.QDialog()
    paperinputui = paperinputdialog.Ui_PaperInputDialog()
    paperinputui.setupUi(PaperInputDialog)

    ModifyDialog = QtGui.QDialog()
    modifyui = modifydialog.Ui_ModifyDialog()
    modifyui.setupUi(ModifyDialog)

    ResultDialog = QtGui.QDialog()
    resultui = resultdialog.Ui_ResultDialog()
    resultui.setupUi(ResultDialog)

    PaperScheduleDialog = QtGui.QDialog()
    paperscheduleui = paperschedule.Ui_PaperScheduleDialog()
    paperscheduleui.setupUi(PaperScheduleDialog)
    paperscheduleui.paperWidthEdit = {}
    paperscheduleui.paperCustomerEdit = {}
    paperscheduleui.editCount = 2
    for i in range(0,10):
        paperscheduleui.paperWidthEdit[i] = QtGui.QLineEdit()
        paperscheduleui.paperWidthEdit[i].setObjectName(_fromUtf8("paperWidthEdit_"+str(i+1)))
        paperscheduleui.paperWidthEdit[i].setVisible(False)
        paperscheduleui.paperCustomerEdit[i] = QtGui.QLineEdit()
        paperscheduleui.paperCustomerEdit[i].setObjectName(_fromUtf8("paperCustomerEdit_"+str(i+1)))
        paperscheduleui.paperCustomerEdit[i].setVisible(False)
        
    for i in range(paperscheduleui.editCount):
        paperscheduleui.gridLayout.addWidget(paperscheduleui.paperWidthEdit[i], 3, i+1, 1, 1)
        paperscheduleui.gridLayout.addWidget(paperscheduleui.paperCustomerEdit[i], 4, i+1, 1, 1)
        paperscheduleui.paperWidthEdit[i].setVisible(True)
        paperscheduleui.paperCustomerEdit[i].setVisible(True)
    #PaperScheduleDialog.exec_()

    ui.systemStatusComboBox.currentIndexChanged.connect(lambda: on_combox_status(model, ui.systemStatusComboBox.currentIndex()+1))
    ui.paperInputPushButton.clicked.connect(lambda: on_inputbutton_push())
    paperinputui.paperInputButtonBox.accepted.connect(lambda: on_paperinput_send(ui, paperinputui, model))
    ui.tableView.verticalHeader().sectionClicked.connect(on_tableView_horizontalHeader_sectionClicked)
    modifyui.resultbuttonBox.accepted.connect(on_modify_send)
    modifyui.transferpushButton.clicked.connect(on_transfer_push)
    paperscheduleui.paperInputButtonBox.accepted.connect(on_paperschedule_send)
    paperscheduleui.paperPlus.clicked.connect(on_paperschedule_plus)

    MainWindow.show()
    sys.exit(app.exec_())