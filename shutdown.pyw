# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shutdown.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(269, 166)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 30, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 30, 47, 13))
        self.label_3.setObjectName("label_3")
        self.ore = QtWidgets.QLineEdit(self.centralwidget)
        self.ore.setGeometry(QtCore.QRect(40, 50, 51, 21))
        self.ore.setObjectName("ore")
        self.minuti = QtWidgets.QLineEdit(self.centralwidget)
        self.minuti.setGeometry(QtCore.QRect(110, 50, 51, 21))
        self.minuti.setObjectName("minuti")
        self.secondi = QtWidgets.QLineEdit(self.centralwidget)
        self.secondi.setGeometry(QtCore.QRect(180, 50, 51, 21))
        self.secondi.setObjectName("secondi")
        self.calcola = QtWidgets.QPushButton(self.centralwidget)
        self.calcola.setGeometry(QtCore.QRect(40, 80, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.calcola.setFont(font)
        self.calcola.setObjectName("calcola")
        self.calcola_2 = QtWidgets.QPushButton(self.centralwidget)
        self.calcola_2.setGeometry(QtCore.QRect(140, 80, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.calcola_2.setFont(font)
        self.calcola_2.setObjectName("calcola_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 270, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Hours"))
        self.label_2.setText(_translate("MainWindow", "Minutes"))
        self.label_3.setText(_translate("MainWindow", "Seconds"))
        self.calcola.setText(_translate("MainWindow", "Shutdown"))
        self.calcola_2.setText(_translate("MainWindow", "Revert"))

        self.calcola.clicked.connect(self.shutdown)
        self.calcola_2.clicked.connect(self.revertz)
    
    def shutdown(self):
        h=self.ore.text()
        m=self.minuti.text()
        s=self.secondi.text()
        if h=='':
            h=0
        if m=='':
            m=0
        if s=='':
            s=0
        sectot=int(h)*3600 + int(m)*60 + int(s) 
        comando='shutdown -s -t '+str(sectot)
        print(comando)
        os.system(comando)
    def revertz(self):
        os.system('shutdown -a')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
