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


nameList = ["批號","紙幅(mm)","顆數","規格(基重條數)","重量(kg)","原基重(gsm)","狀態","米數(m)"]

def DBSetup():
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(os.getcwdu()+os.sep+'papers.sqlite')
    db.open()
    return db

def SQLModelSetup(db,status):
    model = mySqlTableModel(None,db)
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

def on_inputbutton_push(PaperInputDialog):
    if ui.systemStatusComboBox.currentIndex() == 0:
        paperinputui.groupNumberEdit.clear()
        paperinputui.paperLengthEdit.clear()
        paperinputui.paperRollNumberEdit.clear()
        paperinputui.paperSpecEdit.clear()
        paperinputui.paperWeighPerUnitEdit.clear()
        paperinputui.paperWeightEdit.clear()
        paperinputui.paperWidthEdit.clear()
        PaperInputDialog.exec_()
    elif ui.systemStatusComboBox.currentIndex() == 1:
        paperscheduleui.paperLengthEdit.clear()
        paperscheduleui.paperRollNumberEdit.clear()
        paperscheduleui.paperWeightEdit.clear()
        paperscheduleui.paperWidthEdit.clear()
        paperscheduleui.paperLengthEdit_2.clear()
        paperscheduleui.paperRollNumberEdit_2.clear()
        paperscheduleui.paperWeightEdit_2.clear()
        paperscheduleui.paperWidthEdit_2.clear()
        PaperScheduleDialog.exec_()
    else:
        pass


def on_paperinput_send(ui, paperinputui, model):
#    print paperinputui.paperSpecEdit.text()
    try:
        database.InputPaper(paperinputui.groupNumberEdit.text(),\
            paperinputui.paperWidthEdit.text(), paperinputui.paperRollNumberEdit.text(),\
            paperinputui.paperSpecEdit.text(), paperinputui.paperWeightEdit.text(),\
            paperinputui.paperWeighPerUnitEdit.text(), paperinputui.paperLengthEdit.text(),\
            str(ui.systemStatusComboBox.currentIndex()+1))
        resultui.resultlabel.setText(_translate("resultui", "成功", None))
        #resultui.resultlabel.setAlignment()
        #resultui.resultlabel.adjustSize()
    except Exception,e:
        print e
        resultui.resultlabel.setText(_translate("resultui", "失敗，請檢查輸入", None))
        #resultui.resultlabel.adjustSize()
    model.select()
    ResultDialog.exec_()


def on_tableView_horizontalHeader_sectionClicked(index):
    model.currentSelectedIndex = index
    if model.record(index).value('paper_status') == 1:
        modifyui.transfercheckBox.setText(_translate("modifyui", "入庫", None))
        modifyui.transfercheckBox.setDisabled(False)
        modifyui.transfercheckBox.setVisible(True)
    elif model.record(index).value('paper_status') == 3:
        modifyui.transfercheckBox.setText(_translate("modifyui", "出貨", None))
        modifyui.transfercheckBox.setDisabled(False)
        modifyui.transfercheckBox.setVisible(True)
    elif model.record(index).value('paper_status') == 4:
        modifyui.transfercheckBox.setText(_translate("modifyui", "出貨", None))
        modifyui.transfercheckBox.setDisabled(False)
        modifyui.transfercheckBox.setVisible(True)
    elif model.record(index).value('paper_status') == 5:
        modifyui.transfercheckBox.setText(_translate("modifyui", "完工", None))
        modifyui.transfercheckBox.setDisabled(False)
        modifyui.transfercheckBox.setVisible(True)
    elif model.record(index).value('paper_status') == 6:
        modifyui.transfercheckBox.setText(_translate("modifyui", "完工", None))
        modifyui.transfercheckBox.setDisabled(False)
        modifyui.transfercheckBox.setVisible(True)
    else :
        modifyui.transfercheckBox.setDisabled(True)
        modifyui.transfercheckBox.setVisible(False)

#    print model.record(index).value(0)
    ModifyDialog.exec_()

def on_modify_send():
    if modifyui.deletecheckBox.isChecked() == True:
        #print model.record(model.currentSelectedIndex).value('paper_spec')
        modifyui.deletecheckBox.setChecked(False)
        model.removeRow(model.currentSelectedIndex)
        return

    if modifyui.transfercheckBox.isChecked() == True:
        if model.record(model.currentSelectedIndex).value('paper_status') == 1:
            record = QtSql.QSqlRecord(model.record(model.currentSelectedIndex))
            record.setValue('paper_status', 2)
            model.setRecord(model.currentSelectedIndex, record)
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
        modifyui.transfercheckBox.setChecked(False)
    else:
        pass
    model.submitAll()

def on_paperschedule_send():
    record_1 = QtSql.QSqlRecord(model.record(model.currentSelectedIndex))
    record_1.setValue('paper_status', 5)
    record_1.setValue('paper_width', int(paperscheduleui.paperWidthEdit.text()))
    record_1.setValue('paper_weight', int(paperscheduleui.paperWeightEdit.text()))
    record_1.setValue('paper_length', int(paperscheduleui.paperLengthEdit.text()))
    record_1.setValue('paper_roll_number', int(paperscheduleui.paperRollNumberEdit.text()))
    record_2 = QtSql.QSqlRecord(model.record(model.currentSelectedIndex))
    record_2.setValue('paper_status', 6)
    record_2.setValue('paper_width', int(paperscheduleui.paperWidthEdit_2.text()))
    record_2.setValue('paper_weight', int(paperscheduleui.paperWeightEdit_2.text()))
    record_2.setValue('paper_length', int(paperscheduleui.paperLengthEdit_2.text()))
    record_2.setValue('paper_roll_number', int(paperscheduleui.paperRollNumberEdit_2.text()))
    model.insertRecord(-1, record_1)
    model.insertRecord(-1, record_2)
    if int(paperscheduleui.paperRollNumberEdit.text()) \
            == model.record(model.currentSelectedIndex).value('paper_roll_number'):
        model.removeRow(model.currentSelectedIndex)
    else:
        record = QtSql.QSqlRecord(model.record(model.currentSelectedIndex))
        record.setValue('paper_weight', model.record(model.currentSelectedIndex).value('paper_weight') \
            - int(paperscheduleui.paperWeightEdit.text()) - int(paperscheduleui.paperWeightEdit_2.text()))
        record.setValue('paper_length', model.record(model.currentSelectedIndex).value('paper_length') - int(paperscheduleui.paperLengthEdit.text()))
        record.setValue('paper_roll_number', model.record(model.currentSelectedIndex).value('paper_roll_number') - int(paperscheduleui.paperRollNumberEdit.text()))
        model.setRecord(model.currentSelectedIndex, record)
    model.submitAll()



def LayoutLogicSetup(ui,status):
    db = DBSetup()
    model = SQLModelSetup(db, ui.systemStatusComboBox.currentIndex()+1)

    TableViewSetup(ui, model)
    PaperInputDialog = QtGui.QDialog()
    paperinputui = paperinputdialog.Ui_PaperInputDialog()
    paperinputui.setupUi(PaperInputDialog)
    ui.systemStatusComboBox.currentIndexChanged.connect(lambda: on_combox_status(model, ui.systemStatusComboBox.currentIndex()+1))
    ui.paperInputPushButton.clicked.connect(lambda: on_inputbutton_push(PaperInputDialog))
    paperinputui.paperInputButtonBox.accepted.connect(lambda: on_paperinput_send(ui, paperinputui, model))
    ui.tableView.verticalHeader().sectionClicked.connect(on_tableView_horizontalHeader_sectionClicked)


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

    ui.systemStatusComboBox.currentIndexChanged.connect(lambda: on_combox_status(model, ui.systemStatusComboBox.currentIndex()+1))
    ui.paperInputPushButton.clicked.connect(lambda: on_inputbutton_push(PaperInputDialog))
    paperinputui.paperInputButtonBox.accepted.connect(lambda: on_paperinput_send(ui, paperinputui, model))
    ui.tableView.verticalHeader().sectionClicked.connect(on_tableView_horizontalHeader_sectionClicked)
    modifyui.resultbuttonBox.accepted.connect(on_modify_send)
    paperscheduleui.paperInputButtonBox.accepted.connect(on_paperschedule_send)

    MainWindow.show()
    sys.exit(app.exec_())