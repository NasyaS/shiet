import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('Project.ui',self)
        

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.textEdit_2.clear()
        massive=self.textEdit.toPlainText().split('\n')
        result=''
        letters=['а','е','ё','у','ы','и','о','ю','я','э']
        for string in massive:
            count=0
            for i in string.lower():
                for lett in letters:
                    if (i==lett): count+=1
            if(count>0):
                result=result+string+' - '+str(count)+' слогов'+'\n'
            else:
                result=result+'\n'
        self.textEdit_2.setText(result)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
