import os
os.system("cls")
import random as rd
from PyQt5.QtWidgets import ( 
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit,QComboBox,
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

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        # self.setGeometry(1300,200,400,700)
        self.setStyleSheet("background-color:#303670;")
        self.vbox = QVBoxLayout()

        self.label1 = QLabel("Restoran Menyusi")
        self.label1.setStyleSheet(label1_style)
        self.vbox.addWidget(self.label1)

        self.set_combo()
        self.label2 = QLabel("Tanlangan ovqat: ")
        self.label2.setStyleSheet(label2_style)
        self.vbox.addWidget(self.label2)

        self.btn1 = QPushButton("Tugma 1")
        self.btn1.setStyleSheet(btn_style)
        self.vbox.addWidget(self.btn1)
        self.vbox.addSpacing(30)

        self.setLayout(self.vbox)
    
    def set_combo(self):
        self.combo = QComboBox()
        # self.combo.addItem("Osh")
        # self.combo.addItem("Shashlik")
        # self.combo.addItem("Mastava")
        # self.combo.addItem("Sho'rva")
        # self.combo.addItem("Lag'mon")

        self.combo.addItems(["Osh", "Shashlik", "Mastava","Sho'rva", "Lag'mon"])

        self.combo.setStyleSheet(combo_style)
        self.combo.currentTextChanged.connect(self.combo_changed)

        self.vbox.addWidget(self.combo)
    def combo_changed(self):
        text = self.combo.currentText()
        self.label2.setText(f"Tanlangan ovqat: {text}")

        


app = QApplication([])

win = Window()
win.show()
app.exec_()
