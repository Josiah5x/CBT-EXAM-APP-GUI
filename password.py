
from functools import partial
import sys, time
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


DURATION_INT = 600
def secs_to_minsec(secs: int):
    mins = secs // 60
    secs = secs % 60
    minsec = f'{mins:02}:{secs:02}'
    return minsec


class Button(QtWidgets.QPushButton):
    pass
class Radio_Button(QtWidgets.QRadioButton):
    pass


class SchoolCBTMain(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.top=80 
        self.left=20
        self.width = 1365
        self.height=600
        self.WindowApp()

    def WindowApp(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowTitle('Gold Concept CBT App')
        # self.setStyleSheet('background: ;')
        self.conn = sqlite3.connect('gold_concept.db')
        self.cursors = self.conn.cursor()
        # print(' database open successfully')
        # confirmed = input('Search: ')
        # self.cursor = self.conn.execute("SELECT questionid, question, option1, option2, option3, option4 FROM gold_concept")
        # # for row in cursor:
        # #     self.questionData = row
        
        self.group_btn = QtWidgets.QButtonGroup()
        self.group_radiobtn = QtWidgets.QButtonGroup()

        with open("data.json") as f:
            self.questionData = json.load(f)

        # self.questionData = json.load(f)

        self.time_left_int = DURATION_INT
        self.myTimer = QtCore.QTimer(self)
        self.qno=0



        layout = QGridLayout(self)
        self.setLayout(layout)
        menubar = QMenuBar(self)
        layout.addWidget(menubar, 0, 0)
        actionFile = menubar.addMenu("File")
        actionFile.addAction("New")
        actionFile.addSeparator()
        actionFile.addAction("Quit")
        menubar.addMenu("Edit")
        menubar.addMenu("View")
        menubar.addMenu("Help")
        

        # self.timeshow = QFrame(self)
        # self.timeshow.setGeometry(1250, 30, 150, 750)
        # self.timeshow.setStyleSheet('background: #ccc;')
        

        self.groupprofile = QFrame(self)
        self.groupprofile.setGeometry(1, 30, 255, 750)
        self.groupprofile.setStyleSheet('background: rgb(46, 52, 54);')
        

        self.startquiz1 = QtWidgets.QPushButton(self.groupprofile)
        self.startquiz1.setGeometry(QtCore.QRect(20, 250, 201, 36))
        self.startquiz1.setText("Microsoft")
        self.startquiz1.setStyleSheet('background: green; color: #fff')
        # self.startquiz.clicked.connect(self.closeReg)

        self.startquiz2 = QtWidgets.QPushButton(self.groupprofile)
        self.startquiz2.setGeometry(QtCore.QRect(20, 286, 201, 36))
        self.startquiz2.setText("Excell")
        self.startquiz2.setStyleSheet('background: green; color: #fff')
        # self.startquiz.clicked.connect(self.closeReg)

        self.startquiz3 = QtWidgets.QPushButton(self.groupprofile)
        self.startquiz3.setGeometry(QtCore.QRect(20, 322, 201, 36))
        self.startquiz3.setText("Corel Draw")
        self.startquiz3.setStyleSheet('background: green; color: #fff')
        # self.startquiz.clicked.connect(self.closeReg)

        self.startquiz4 = QtWidgets.QPushButton(self.groupprofile)
        self.startquiz4.setGeometry(QtCore.QRect(20, 358, 201, 36))
        self.startquiz4.setText("Web Browser")
        self.startquiz4.setStyleSheet('background: green; color: #fff')
        # self.startquiz.clicked.connect(self.closeReg)

        self.startquiz5 = QtWidgets.QPushButton(self.groupprofile)
        self.startquiz5.setGeometry(QtCore.QRect(20, 394, 201, 36))
        self.startquiz5.setText("Email Basic")
        self.startquiz5.setStyleSheet('background: green; color: #fff')
        # self.startquiz.clicked.connect(self.closeReg)

        self.logolabel = QLabel(self.groupprofile)
        self.logolabel.setFont(QtGui.QFont('Fontdinerdotcom Luvable',50,))
        self.logolabel.setText('GOLD')
        # self.logolabel.setAlignment(Qt.AlignCenter)
        self.logolabel.setGeometry(40, 25, 400, 60)
        self.logolabel.setStyleSheet('color:  rgb(252, 175, 62);')
        # self.vlayout2.addWidget(self.logolabel)
        # self.group2.setLayout(self.logolabel)

        self.logolabel2 = QLabel(self.groupprofile)
        self.logolabel2.setFont(QtGui.QFont('Dyuthi',12,))
        self.logolabel2.setText('Concept Computer & ICT Academy')
        # self.logolabel2.setAlignment(Qt.AlignCenter)
        self.logolabel2.setGeometry(10, 90, 400, 60)
        self.logolabel2.setStyleSheet('color: #fff;')
        # self.vlayout2.addWidget(self.logolabel2)
        # self.group2.setLayout(self.logolabel)

        

        # self.group2 = QGroupBox(self)
        # self.group2.setGeometry(260, 30, 1100, 400)
        # self.group2.setStyleSheet('background: #ddd')


        self.forwardbtn = QtWidgets.QPushButton(self)
        self.forwardbtn.setGeometry(QtCore.QRect(800, 432, 80, 36))
        self.forwardbtn.setText(">")
        self.forwardbtn.setFont(QtGui.QFont('consola',12,))
        self.forwardbtn.setStyleSheet('background: green; color: #fff')
        self.forwardbtn.clicked.connect(self.next_btn)
        # self.vlayout.addWidget(self.forwardbtn)


        self.forwardlabel = QLabel(self)
        self.forwardlabel.setFont(QtGui.QFont('consola',12,))
        self.forwardlabel.setText('Next')
        self.forwardlabel.setAlignment(Qt.AlignCenter)
        self.forwardlabel.setGeometry(740, 460, 200, 36)

        self.backwardbtn = QtWidgets.QPushButton(self)
        self.backwardbtn.setGeometry(QtCore.QRect(700, 432, 80, 36))
        self.backwardbtn.setText("<")
        self.backwardbtn.setFont(QtGui.QFont('consola',12,))
        self.backwardbtn.setStyleSheet('background: green; color: #fff')
        self.backwardbtn.clicked.connect(self.previous_btn)
        # self.vlayout.addWidget(self.backwardbtn)

        self.backwardlabel = QLabel(self)
        self.backwardlabel.setFont(QtGui.QFont('consola',12,))
        self.backwardlabel.setText('Previous')
        self.backwardlabel.setAlignment(Qt.AlignCenter)
        self.backwardlabel.setGeometry(640, 460, 200, 36)



        self.group2 = QGroupBox(self)
        self.group2.setGeometry(260, 30, 1100, 400)
        self.group2.setStyleSheet('background: #ddd')

        self.vlayout = QVBoxLayout(self)
        self.vlayout.addStretch(0)
        self.group2.setLayout(self.vlayout)


        self.username = QLabel(self.group2)
        self.username.setFont(QtGui.QFont('consola',12,))
        # self.username.setText('Josiah')
        self.username.setAlignment(Qt.AlignCenter)
        self.username.setGeometry(645, 5, 252, 35)
        self.username.setStyleSheet('background: #F5FBFF; color: #333')

        self.imagelabel = QLabel(self.group2)
        # self.imagelabel.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap("user.png")
        self.imagelabel.setPixmap(self.pixmap)
        self.imagelabel.setGeometry(645, 8, 30, 30)
        # self.vlayout2.addWidget(self.imagelabel)


        self.startquiz = QtWidgets.QPushButton(self.group2)
        self.startquiz.setGeometry(5, 8, 101, 36)
        self.startquiz.setText("Submit Quiz")
        self.startquiz.setStyleSheet('background: green; color: #fff')
        self.startquiz.clicked.connect(self.showDialog)


        self.starttimequizframe = QFrame(self.group2)
        self.starttimequizframe.setGeometry(990, 8, 101, 120)
        self.starttimequizframe.setStyleSheet('background: #e8ffe8; color: #fff')

        self.timelogo = QLabel(self.starttimequizframe)
        # self.timelogo.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap("alert_32x32.png")
        self.timelogo.setPixmap(self.pixmap)
        self.timelogo.setGeometry(35, 1, 101, 36)

        self.starttimequiz = QLabel(self.starttimequizframe)
        self.starttimequiz.setFont(QtGui.QFont('consola', 20))
        self.starttimequiz.setAlignment(Qt.AlignCenter)
        self.starttimequiz.setGeometry(0, 50, 101, 80)
        self.starttimequiz.setStyleSheet('background: #333; color: #fff')
        # self.vlayout.addWidget(self.starttimequiz)


        self.countlabel = QLabel(self.group2)
        self.countlabel.setFont(QtGui.QFont('consola',12,))
        # self.countlabel.setText('CBT Exam')
        self.countlabel.setAlignment(Qt.AlignCenter)
        self.countlabel.setGeometry(450, 8, 60, 36)
        # self.countlabel.setStyleSheet('background: rgb(46, 52, 54);')
        # self.vlayout.addWidget(self.countlabel)


        self.questionLabel = QtWidgets.QLabel(self)
        # self.questionLabel.setGeometry(1, 1, 800, 60)
        self.questionLabel.setFont(QtGui.QFont('aakar', 14))
        self.questionLabel.setStyleSheet('background: #f7fcf5')
        self.vlayout.addWidget(self.questionLabel)


        self.radiobtn = QRadioButton(self)
        self.radiobtn.setFont(QtGui.QFont('aakar', 13))
        # self.radiobtn.setStyleSheet('background: #f7fcf5')
        # self.radiobtn.clicked.connect(self.jsonfile)
        self.radiobtn.toggled.connect(self.update)
        self.radiobtn.setChecked(False)
        # self.radiobtn.setGeometry(540, 420, 200, 36)
        self.vlayout.addWidget(self.radiobtn)

        self.radiobtn2 = QRadioButton(self)
        self.radiobtn2.setFont(QtGui.QFont('aakar', 13))
        self.radiobtn2.setChecked(False)
        # self.radiobtn2.setStyleSheet('background: #f7fcf5')
        # self.radiobtn2.clicked.connect(self.jsonfile)
        self.radiobtn2.toggled.connect(self.update)
        self.vlayout.addWidget(self.radiobtn2)

        self.radiobtn3 = QRadioButton( self)
        self.radiobtn3.setFont(QtGui.QFont('aakar', 13))
        self.radiobtn3.setChecked(False)
        # self.radiobtn3.clicked.connect(self.jsonfile)
        self.radiobtn3.toggled.connect(self.update)
        # self.radiobtn3.setStyleSheet('background: #f7fcf5')
        self.vlayout.addWidget(self.radiobtn3)

        self.radiobtn4 = QRadioButton( self)
        self.radiobtn4.setFont(QtGui.QFont('aakar', 13))
        self.radiobtn4.setChecked(False)
        # self.radiobtn4.clicked.connect(self.jsonfile)
        self.radiobtn4.toggled.connect(self.update)
        # self.radiobtn4.setStyleSheet('background: #f7fcf5')
        self.vlayout.addWidget(self.radiobtn4)


        self.dic = self.questionData[1]

        self.startTimer()
        self.check(i=1)
        self.initalizingQuestion(self)
        # self.jsonfile(0)
        # self.previous_btn()

        self.groupbutton = QGroupBox(self)
        self.groupbutton.setStyleSheet('background: #e8ffe8')
        self.groupbutton.setTitle("Quick Navigation")
        self.groupbutton.setFont(QtGui.QFont('consola',15,))
        self.groupbutton.setGeometry(260, 500, 1100, 250)
        # self.groupbutton.setStyleSheet('background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.509, y2:0, stop:0 rgba(8, 120, 48, 255), stop:1 rgba(0, 168, 119, 255));; color: #fff;')
        self.layoutbutton = QGridLayout(self)
        # self.layoutbutton.addStrech(1)
        self.groupbutton.setLayout(self.layoutbutton)

        self.lent = len(self.questionData)
        self.g_i=1
      
        self.group_btn.buttonClicked[int].connect(self.slot)
    
        self.buttonlist = int
        for self.buttonlist in range(self.lent):
            self.orgLen = self.buttonlist+1
            self.button = Button(f'{self.orgLen}')
            self.button.clicked.connect(partial(self.check, self.g_i))
            self.button.setCheckable(True)
            # self.button.setStyleSheet("QPushButton {background: #; color: #fff}""QPushButton:Hover {background: yellow;}")
            # if self.buttonlist == 0:
                # self.button.setChecked(True)
                # self.button.setStyleSheet("QPushButton {background: green; color: #fff;}")
            self.group_radiobtn.addButton(self.button, self.orgLen)
            self.layoutbutton.addWidget(self.button, 0, self.orgLen+1)
            self.g_i+=1
            if self.g_i == self.lent:break

            # ////////////////////Radio Button////////////////////////
    def initalizingQuestion(self, objs):
            self.ch = ["A:", "B:", "C:", "D:"]
            self.opt = ["option1","option2","option3","option4"]
            # self.qradio = [self.radiobtn, self.radiobtn2, self.radiobtn3, self.radiobtn4]

            self.radiobtn.setText(f'{self.ch[0]} {self.dic[self.opt[0]]}')
            self.radiobtn2.setText(f'{self.ch[1]} {self.dic[self.opt[1]]}')
            self.radiobtn3.setText(f'{self.ch[2]} {self.dic[self.opt[2]]}')
            self.radiobtn4.setText(f'{self.ch[3]}{self.dic[self.opt[3]]}')

            for btn in self.group_btn.buttons():
                if btn is self.group_btn.button(objs):
                    if btn ==
                    btn.setCheckable(True)
                    btn.setStyleSheet("QPushButton {background: green; color: #fff;}" "QPushButton:Hover {background: yellow;}")
            
                
        
            # ############################################

    def slot(self, objs):
        for btn in self.group_btn.buttons():
            if btn is self.group_btn.button(objs):
                btn.setStyleSheet("QPushButton {background: green; color: #fff;}" "QPushButton:Hover {background: yellow;}")
           

    def save_my_data(self, question, option1, option2, option3, option4, answer):
        self.query = "INSERT INTO gold_concept VALUES (?,?,?,?,?,?)"
        self.params = (None, question, option1, option2, option3, option4, answer)
        self.cursors.execute(self.query, self.params)
        self.conn.commit()

    def showDialog(self):
        reply = QMessageBox.question(self, 'Information', """ Welcome to GOLD Concept CBT Exam
        You Are about to Start
        Click Yes to (start) and No to (Ignor) """, QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.jsonfile(1)
            self.time_left_int = DURATION_INT
            self.myTimer.timeout.connect(self.timerTimeout)
            self.myTimer.start(1000)
        else:
            pass
            

    def startTimer(self):
        self.time_left_int = DURATION_INT
        self.myTimer.timeout.connect(self.timerTimeout)
        self.myTimer.start(1000)
        
    def timerTimeout(self):
        self.time_left_int -= 1

        if self.time_left_int == 0:
            self.time_left_int = DURATION_INT

        self.update_gui()

    def update_gui(self):
        minsec = secs_to_minsec(self.time_left_int)
        self.starttimequiz.setText(minsec)



    def check(self, i):
        self.qno=i
        try:
                
                self.diclist = self.questionData[i]
           
                self.id = 'id'
                z = 'question'
                size = len(self.questionData)-1

                self.countlabel.setText(f'{self.diclist[self.id]}/{size}')
                ls = f'Question {self.diclist[self.id]} \n \n {self.diclist[z]}'
                self.questionLabel.setText(ls)
  
           
           
        except IndexError:
            print('End of question')


    def next_btn(self):
        self.qno+=1
        if self.qno == 0:
            self.qno = +1
        self.diclist = self.questionData[self.qno]

        self.id = 'id'
        z = 'question'

        self.countlabel.setText(f'{self.diclist[self.id]}/30')
        ls = f'Question {self.diclist[self.id]} \n \n {self.diclist[z]}'
        self.questionLabel.setText(ls)
        # 
        self.ch = ["A:", "B:", "C:", "D:"]
        self.opt = ["option1","option2","option3","option4"]

        self.radiobtn.setText(f'{self.ch[0]} {self.diclist[self.opt[0]]}')
        self.radiobtn2.setText(f'{self.ch[1]} {self.diclist[self.opt[1]]}')
        self.radiobtn3.setText(f'{self.ch[2]} {self.diclist[self.opt[2]]}')
        self.radiobtn4.setText(f'{self.ch[3]} {self.diclist[self.opt[3]]}')


        vbox2 = QtWidgets.QVBoxLayout(self)
        vbox2.addLayout(self.vlayout)
        # vbox2.addWidget(stackedwidget2)
        self.group2.setLayout(vbox2)

    def clear(self):
      item = self.layout.itemAt(2)
      if item != None :
          widget = item.widget()
          if widget != None:
              self.layout.removeWidget(widget)
              widget.deleteLater() 

    def previous_btn(self):
        self.qno-=1
        if self.qno == 0:
            self.qno = -1

        self.diclist = self.questionData[self.qno]
      
        self.id = 'id'
        z = 'question'

        self.countlabel.setText(f'{self.diclist[self.id]}/30')
        ls = f'Question {self.diclist[self.id]} \n \n {self.diclist[z]}'
        self.questionLabel.setText(ls)
        self.ch = ["A:", "B:", "C:", "D:"]
        self.opt = ["option1","option2","option3","option4"]

        self.radiobtn.setText(f'{self.ch[0]} {self.diclist[self.opt[0]]}')
        self.radiobtn2.setText(f'{self.ch[1]} {self.diclist[self.opt[1]]}')
        self.radiobtn3.setText(f'{self.ch[2]} {self.diclist[self.opt[2]]}')
        self.radiobtn4.setText(f'{self.ch[3]} {self.diclist[self.opt[3]]}')


    def update(self):
        # get the radio button the send the signal
        rb = self.sender()

        # check if the radio button is checked
        if rb.isChecked():
            print(f'You selected {rb.text()}')

    def jsonfile(self, i):
        try:
            # self.qno+=1

            print(f'######{self.questionLabel.text()}')
            if self.radiobtn.text() == self.radiobtn.text():

                if self.radiobtn.isChecked() == True: 
                    print(self.radiobtn.text())
                    self.questionData.update({"answer": self.radiobtn.text()})
                    c = self.questionData.keys()
                    with open('exam.txt', 'a') as self.mykey:
                        self.key = self.mykey.write(f'{self.questionLabel.text()} \n {self.radiobtn.text()} \n')

            if self.radiobtn2.text() == self.radiobtn2.text():
                if self.radiobtn2.isChecked() == True:
                    print(self.radiobtn2.text())
                    with open('exam.txt', 'a') as self.mykey:
                        self.key = self.mykey.write(f'{self.questionLabel.text()} \n {self.radiobtn2.text()} \n')

            if self.radiobtn3.text() == self.radiobtn3.text():
                if self.radiobtn3.isChecked() == True:
                    print(self.radiobtn3.text())
                    with open('exam.txt', 'a') as self.mykey:
                        self.key = self.mykey.write(f'{self.questionLabel.text()} \n {self.radiobtn3.text()} \n')

            if self.radiobtn4.text() == self.radiobtn4.text():
                if self.radiobtn4.isChecked() == True:
                    print(self.radiobtn4.text())
                    with open('exam.txt', 'a') as self.mykey:
                        self.key = self.mykey.write(f'{self.questionLabel.text()} \n {self.radiobtn4.text()} \n')

            # self.answer()
            self.radiobtn.setCheckable(True)
            self.radiobtn2.setCheckable(True)
            self.radiobtn3.setCheckable(True)
            self.radiobtn4.setCheckable(True)
        except:
            print()
            
        
        # except IndexError:
        #     print('Congratulation... You are done with your Quiz')
            # self.showDialog()
        
        
    


class LogForm(QWidget):
    def __init__(self):
        super().__init__()

        self.top=80 
        self.left=20
        self.width = 1365
        self.height=600
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # self.setWindowModality(Qt.ApplicationModal)
        # self.setFixedSize(self.width, self.height)
        
        # self.setStyleSheet("background: #000;")

        self.setStyleSheet("background-image: url(img/lib1.jpg);")
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowTitle('Login Form')

        self.questionLabel = QtWidgets.QLabel(self)
        self.questionLabel.setGeometry(QtCore.QRect(10, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.questionLabel.setFont(font)
        self.questionLabel.setObjectName("questionLabel")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 231, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(550, 150, 331, 231))
        self.groupBox.setStyleSheet('background: #f2f7d9')
        self.groupBox.setObjectName("groupBox")
        
        self.username = QtWidgets.QLineEdit(self.groupBox)
        self.username.setGeometry(QtCore.QRect(10, 30, 311, 36))
        self.username.setObjectName("username")
        self.username.setPlaceholderText("username")
        self.username.setFont(QtGui.QFont('Arial', 13))
        self.username.setStyleSheet('background: #fff')

        self.password = QtWidgets.QLineEdit(self.groupBox)
        self.password.setGeometry(QtCore.QRect(10, 80, 311, 36))
        self.password.setObjectName("password")
        self.password.setPlaceholderText("password")
        self.password.setFont(QtGui.QFont('Arial', 13))
        self.password.setStyleSheet('background: #fff')

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(70, 150, 201, 36))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet('background: green; color: #fff')
        self.pushButton.clicked.connect(self.closeReg)
        
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(550, 376, 330, 8))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.pushButton.setText("Submit")
        self.questionLabel.setText("Gold")
        self.label_2.setText("Concept Computer & ICT Accademy")
        self.groupBox.setTitle("Login Form")

    def closeReg(self):
        if self.username.text() == 'joe' and self.password.text() == '123':
            

            for i in range(50):
                time.sleep(0.03)
                self.progressBar.setValue(i)
            self.close()

            wLog = LogForm()
            wLog.close()

            window = SchoolCBTMain()
            window.username.setText(f'Welcome {self.username.text()}')
            window.show()

            # windowForms = Window_Form()
            # windowForms.close()

            # wReg = RegForm()
            # wReg.close()

            


            

            
            # window.username.setText(self.win.username.text())


class RegForm(QWidget):
    def __init__(self):
        super().__init__()

        self.left =140
        self.top =200
        self.width =400
        self.height =390
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(self.width, self.height)
        
        self.setStyleSheet("background: #fff;")

        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowTitle('Rgistration Form')

        self.questionLabel = QtWidgets.QLabel(self)
        self.questionLabel.setGeometry(QtCore.QRect(10, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.questionLabel.setFont(font)
        self.questionLabel.setObjectName("questionLabel")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 231, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(30, 70, 331, 231))
        self.groupBox.setStyleSheet('background: #f2f7d9')
        self.groupBox.setObjectName("groupBox")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 80, 311, 36))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet('background: #fff')

        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 311, 36))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet('background: #fff')

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(70, 150, 201, 36))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet('background: green; color: #fff')
        self.pushButton.clicked.connect(self.closeReg)
        
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(30, 300, 330, 8))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.pushButton.setText("Submit")
        self.questionLabel.setText("Gold")
        self.label_2.setText("Concept Computer & ICT Accademy")
        self.groupBox.setTitle("Registration")

    def closeReg(self):
        for i in range(101):
            time.sleep(0.03)
            self.progressBar.setValue(i)
        self.close()

        window = RegForm()
        window.close()

        window = SchoolCBTMain()
        window.show()


        
class Window_Form(QWidget):
    def __init__(self):
        super().__init__()

        self.left =140
        self.top =200
        self.width =800
        self.height =600
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(self.width, self.height)
        
        self.setStyleSheet("background: #fff;")

        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowTitle('Rgistration Form')

        self.logo = QLabel(self)
        self.logo.setFont(QtGui.QFont('Fontdinerdotcom Luvable',80,))
        self.logo.setText('GOLD')
        self.logo.setGeometry(30, 50, 291, 61)
        self.logo.setStyleSheet('color: rgb(193, 125, 17);')

        self.logo2 = QLabel(self)
        self.logo2.setFont(QtGui.QFont('Dyuthi',30,))
        self.logo2.setText('Concept Computer & ICT Academy')
        self.logo2.setGeometry(30, 110, 651, 61)
        self.logo2.setStyleSheet('color: rgb(193, 125, 17);')

        
        self.progressbar = QProgressBar(self)
        self.progressbar.setGeometry(30, 160, 371, 23)

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(30, 170, 361, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(QtGui.QFont('Arial', 13))
        self.pushButton.setStyleSheet('background: #69bf3e; color: #fff')
        self.pushButton.clicked.connect(self.regForm)
        
        self.progressbar2 = QProgressBar(self)
        self.progressbar2.setGeometry(30, 280, 371, 23)
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 170, 361, 91))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setFont(QtGui.QFont('Arial', 13))
        self.pushButton_2.setStyleSheet('background:  rgb(87, 223, 207); color: #fff')
        self.pushButton_2.clicked.connect(self.logForm)

        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 290, 361, 81))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setFont(QtGui.QFont('Arial', 13))
        self.pushButton_3.setStyleSheet('background: rgb(239, 41, 41); color: #fff')

        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 290, 361, 81))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setFont(QtGui.QFont('Arial', 13))
        self.pushButton_4.setStyleSheet('background:  rgb(237, 212, 0); color: #fff')

        self.pushButton.setText("Create Account")
        self.pushButton_2.setText( "Login with Your Account")
        self.pushButton_3.setText( "PushButton")
        self.pushButton_4.setText( "PushButton")

    def regForm(self):
        self.win = RegForm()
        self.win.show()
    
    def logForm(self):
        self.win = LogForm()
        self.win.show()




if __name__=='__main__':
    app = QApplication(sys.argv)
    window = SchoolCBTMain()
    window.show()

    
    # win = LogForm()
    # win.show()
    sys.exit(app.exec_())  