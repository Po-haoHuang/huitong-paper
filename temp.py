# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
from PyQt4 import QtGui, uic
import PyQt4 
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
class MyWindow(QtGui.QDialog):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('paperinput.ui', self)
        self.groupNumber.setText(_translate("PaperInputDialog", "test(m):", None))
        self.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())