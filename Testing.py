import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QRadioButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.qno = 0
        self.qno2 = 1
        self.x = ['A', 'A', 'B', 'C', 'D']
        self.button = QRadioButton(self)
        self.button.setText(self.x[1])
        self.button.setChecked(False)
        self.button.clicked.connect(self.check)
        self.setCentralWidget(self.button)
        # self.check()
    def dcrease(self):
        self.qno-=1
        self.button.setText(self.x[self.qno])
    def check(self):
        self.button.setChecked(False)
        
        while self.qno < 5:
            
            self.qno+=1
                # self.dcrease()
            self.button.setText(self.x[self.qno])
            
            print(self.button.text())
            print(self.qno)
            break
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()