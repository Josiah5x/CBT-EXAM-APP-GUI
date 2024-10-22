from PyQt5 import QtCore, QtWidgets

from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QScrollArea, QPushButton,
 QLineEdit, QTextEdit, QPlainTextEdit, QInputDialog, QMessageBox)
from PyQt5 import QtGui 
from PyQt5.QtGui import QPixmap
from datetime import datetime
from time import strftime
# import mysql.connector
import json
import jsonfile
import sqlite3
# from mysql.connector import Error, errorcode
from PyQt5.QtCore import QObject, Qt, pyqtSignal, QTimer, QTime
from PyQt5.QtWidgets import*
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtCore

QSS = """
Button {
  background-color: #00ff00;
}

Button:checked {
  background-color: #ff0000;
}
"""



class Button(QtWidgets.QPushButton):
    pass
class RadioButton(QtWidgets.QRadioButton):
    pass


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        self.group_radiobutton = QGroupBox(self)
        self.group_radiobutton.setGeometry(20, 30, 1200, 200)
        self.group_radiobutton.setStyleSheet('background: #ddd')
        # ///////////////////////
        self.group_button = QGroupBox(self)
        self.group_button.setGeometry(20, 250, 1200, 200)
        # self.group_button.setStyleSheet('background: #ddd')

        self.vlayout = QVBoxLayout(self)
        self.vlayout.addStretch(0)
        self.group_radiobutton.setLayout(self.vlayout)

        # page1 = QtWidgets.QLabel("page1", alignment=QtCore.Qt.AlignCenter)
        page2 = QtWidgets.QLabel("page2", alignment=QtCore.Qt.AlignCenter)
        page3 = QtWidgets.QLabel("page3", alignment=QtCore.Qt.AlignCenter)

        self.qno=0



        self.label = QtWidgets.QLabel(self)
        # self.label.setGeometry(1, 1, 800, 60)
        self.label.setFont(QtGui.QFont('aakar', 14))
        self.label.setStyleSheet('background: #f7fcf5')
        self.vlayout.addWidget(self.label)

    
        self.radiobtn = QRadioButton(self)
        self.radiobtn.setFont(QtGui.QFont('aakar', 13))
        self.radiobtn.setStyleSheet('background: #f7fcf5')
        # self.radiobtn.clicked.connect(self.jsonfile)
        self.radiobtn.toggled.connect(self.update)
        self.radiobtn.setChecked(False)
        # self.radiobtn.setGeometry(540, 420, 200, 36)
        self.vlayout.addWidget(self.radiobtn)

        self.radiobtn2 = QRadioButton(self)
        self.radiobtn2.setFont(QtGui.QFont('aakar', 13))
        self.radiobtn2.setChecked(False)
        self.radiobtn2.setStyleSheet('background: #f7fcf5')
        # self.radiobtn2.clicked.connect(self.jsonfile)
        self.radiobtn2.toggled.connect(self.update)
        self.vlayout.addWidget(self.radiobtn2)

        self.radiobtn3 = QRadioButton( self)
        self.radiobtn3.setFont(QtGui.QFont('aakar', 13))
        self.radiobtn3.setChecked(False)
        # self.radiobtn3.clicked.connect(self.jsonfile)
        self.radiobtn3.toggled.connect(self.update)
        self.radiobtn3.setStyleSheet('background: #f7fcf5')
        self.vlayout.addWidget(self.radiobtn3)

        self.radiobtn4 = QRadioButton( self)
        self.radiobtn4.setFont(QtGui.QFont('aakar', 13))
        self.radiobtn4.setChecked(False)
        # self.radiobtn4.clicked.connect(self.jsonfile)
        self.radiobtn4.toggled.connect(self.update)
        self.radiobtn4.setStyleSheet('background: #f7fcf5')
        self.vlayout.addWidget(self.radiobtn4)

            
        with open("data.json") as f:
            self.questionData = json.load(f)
        diclist = self.questionData[0]
        
        self.check(i=1)
            
        options = ["option1", "option2", "option3", "option4"]
        # b = [page1, page2]


        # stackedwidget = QtWidgets.QStackedWidget()

        # hlay = QtWidgets.QVBoxLayout()
        # group = QtWidgets.QButtonGroup(self)
        # group.buttonClicked[int].connect(stackedwidget.setCurrentIndex)
        

        # # for i, (option, widget) in enumerate(zip(options, (self.label, self.radiobtn, self.radiobtn2, self.radiobtn3, self.radiobtn4))):
        # for i, (option, widget) in enumerate(zip(diclist, (page2, page3, page3, page3))):
        #     radio_button = RadioButton(text=option, checkable=True)
        #     ix = stackedwidget.addWidget(widget)
        #     group.addButton(radio_button, ix)
        #     hlay.addWidget(radio_button)
        #     if i == 0:
        #         radio_button.setChecked(True)

        # vbox = QtWidgets.QVBoxLayout(self)
        # vbox.addLayout(hlay)
        # vbox.addWidget(stackedwidget)
        # self.group_radiobutton.setLayout(vbox)
     
        # //////////////////////////////////////////////////

        stackedwidget2 = QtWidgets.QStackedWidget()

        hlay2 = QtWidgets.QVBoxLayout()
        group3 = QtWidgets.QButtonGroup(self)
        group3.buttonClicked[int].connect(stackedwidget2.setCurrentIndex)

        for i, (option, widget) in enumerate(zip(options, (page2, page2))):
            button = Button(text=option, checkable=True)
            ix = stackedwidget2.addWidget(widget)
            group3.addButton(button, ix)
            hlay2.addWidget(button)
            if i == 0:
                button.setChecked(True)

        vbox2 = QtWidgets.QVBoxLayout(self)
        vbox2.addLayout(hlay2)
        # vbox2.addWidget(stackedwidget2)
        self.group_button.setLayout(vbox2)


    def check(self, i):
        # self.qno=i
        try:
            diclist = self.questionData[i]
            a = "option1"
            b = "option2"
            c = "option3"
            d = "option4"

            A = f'(A){diclist[a]}'
            B = f'(B){diclist[b]}'
            C = f'(C){diclist[c]}'
            D = f'(D){diclist[d]}'
            self.id = 'id'
            z = 'question'
            size = len(self.questionData)-1

            # self.countlabel.setText(f'{diclist[self.id]}/{size}')
            ls = f'Question {diclist[self.id]} \n \n {diclist[z]}'
            self.label.setText(ls)
            self.radiobtn.setText(A)
            self.radiobtn2.setText(B)
            self.radiobtn3.setText(C)
            self.radiobtn4.setText(D)

        except IndexError:
            print('End of question')



if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    app.setStyleSheet(QSS)
    w = Widget()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())