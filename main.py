import os
os.system("cls")
import random as rd
from PyQt5.QtWidgets import ( 
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit,
    QVBoxLayout, QHBoxLayout
)

btn_style = """
    background-color:#e8e689;
    color:black;
    font-size:20px;
    border-radius:20px;
    border: 2px solid red;
"""

input_style = """
    background-color: white;
    font-size: 20px;
    border: 3px solid black;
"""

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(1300,200,400,700)
        self.setStyleSheet("background-color:#303670;")
        self.vbox = QHBoxLayout()
        

        self.btn1 = QPushButton("Tugma 1")
        self.btn1.setStyleSheet(btn_style)
        self.vbox.addWidget(self.btn1)
        self.vbox.addSpacing(30)


        self.btn2 = QPushButton("Tugma 2")
        self.btn2.setStyleSheet(btn_style)
        self.vbox.addWidget(self.btn2)
        self.vbox.addSpacing(30)

        self.btn3 = QPushButton("Tugma 3")
        self.btn3.setStyleSheet(btn_style)
        self.vbox.addWidget(self.btn3)
        self.vbox.addSpacing(30)

        self.btn4 = QPushButton("Tugma 4")
        self.btn4.setStyleSheet(btn_style)
        self.vbox.addWidget(self.btn4)
        self.vbox.addSpacing(30)

        self.btn5 = QPushButton("Tugma 5")
        self.btn5.setStyleSheet(btn_style)
        self.vbox.addWidget(self.btn5)
        
        self.setLayout(self.vbox)

        


app = QApplication([])

win = Window()
win.show()
app.exec_()
