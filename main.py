import os
os.system("cls")
import random as rd
from PyQt5.QtWidgets import ( 
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit,QComboBox,QCheckBox,QRadioButton,QMessageBox,
    QVBoxLayout, QHBoxLayout
)

win_style = """
    background-color: black;
"""

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

label1_style = """
    font-size: 40px;
    color: white;
    font-family: Impact;
"""

combo_style = """
    font-size: 20px;
    background-color: white;
    color:black;
"""
label2_style = """
    font-size: 20px;
    color: white;
"""

checkbox_style = """
    color:white;
    font-size:15px;
"""


message_style = """
    QMessageBox {
        background-color:white;
        color:black;
        font-size:20px;
    }
"""

class Contacts(QWidget):
    def __init__(self, main_win):
        super().__init__()
        self.main_win = main_win
        self.setGeometry(1350,200,400,700)
        self.setWindowTitle("Kontaktlar")
        self.vbox = QVBoxLayout()

        self.label1 = QLabel("Telefon: +9981234567")
        self.label1.setStyleSheet(combo_style)
        self.label2 = QLabel("Email: example@mail.com")
        self.label2.setStyleSheet(combo_style)
        self.label3 = QLabel("Address: Tashkent")
        self.label3.setStyleSheet(combo_style)

        self.btn1 = QPushButton("Orqaga")
        self.btn1.setStyleSheet(btn_style)
        self.btn1.clicked.connect(self.back_func)


        self.vbox.addWidget(self.label1)
        self.vbox.addWidget(self.label2)
        self.vbox.addWidget(self.label3)
        self.vbox.addWidget(self.btn1)
        self.setLayout(self.vbox)

    def back_func(self):
        self.hide()
        self.main_win.show()
        

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1350,200,400,700)
        self.setStyleSheet(win_style)
        self.vbox = QVBoxLayout()

        self.label1 = QLabel("Bu Asosiy Oyna")
        self.label1.setStyleSheet(label1_style)

        self.btn1 = QPushButton("Contancts")
        self.btn1.clicked.connect(self.open_contact)
        self.btn1.setStyleSheet(btn_style)

        self.vbox.addWidget(self.label1)
        self.vbox.addWidget(self.btn1)

        self.setLayout(self.vbox)
    
    def open_contact(self):
        self.win2 = Contacts(self)
        self.hide()
        self.win2.show()


app = QApplication([])
win = Window()
win.show()
app.exec_()
