import sys
from Project import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.MyFunction)

    def MyFunction(self):
        self.ui.textEdit_2.setText("")
        strings=self.ui.textEdit.toPlainText()
        massive=strings.split('\n')
        result=''
        letters=['а','е','ё','у','ы','и','о','ю','я','э']
        for string in massive:
            count=0
            for i in string.lower():
                for lett in letters:
                    if (i==lett): count=count+1
            if(count>0):
                result=result+string+' - '+str(count)+' слогов'+'\n'
            else:
                result=result+'\n'
        self.ui.textEdit_2.setText(result)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
