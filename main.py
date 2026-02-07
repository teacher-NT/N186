import os
os.system("cls")
import random as rd
from PyQt5.QtWidgets import ( 
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit,QComboBox,QCheckBox,QRadioButton,QMessageBox,
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

        self.set_checkbox()
        self.label3 = QLabel("Tanlangan ichimliklar: ")
        self.label3.setStyleSheet(label2_style)
        self.vbox.addWidget(self.label3)

        self.label4 = QLabel("To'lov turi:")
        self.label4.setStyleSheet(label2_style)
        self.vbox.addWidget(self.label4)
        self.set_radio()

        self.btn1 = QPushButton("Buyurtma qilish")
        self.btn1.setStyleSheet(btn_style)
        self.btn1.clicked.connect(self.show_message)
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
        self.combo.addItems(["Ovqatlar", "Osh", "Shashlik", "Mastava","Sho'rva", "Lag'mon"])
        self.combo.setStyleSheet(combo_style)
        self.combo.currentTextChanged.connect(self.combo_changed)
        self.vbox.addWidget(self.combo)
    def combo_changed(self):
        text = self.combo.currentText()
        self.label2.setText(f"Tanlangan ovqat: {text}")

    def set_checkbox(self):
        self.check1 = QCheckBox("Qora choy")
        self.check1.setStyleSheet(checkbox_style)
        self.check1.stateChanged.connect(self.checkbox_func)
        self.check2 = QCheckBox("Ko'k choy")
        self.check2.setStyleSheet(checkbox_style)
        self.check2.stateChanged.connect(self.checkbox_func)
        self.check3 = QCheckBox("Coffee")
        self.check3.setStyleSheet(checkbox_style)
        self.check3.stateChanged.connect(self.checkbox_func)
        self.check4 = QCheckBox("Suv")
        self.check4.setStyleSheet(checkbox_style)
        self.check4.stateChanged.connect(self.checkbox_func)
        self.check5 = QCheckBox("Kokteyl")
        self.check5.setStyleSheet(checkbox_style)
        self.check5.stateChanged.connect(self.checkbox_func)

        self.vbox.addWidget(self.check1)
        self.vbox.addWidget(self.check2)
        self.vbox.addWidget(self.check3)
        self.vbox.addWidget(self.check4)
        self.vbox.addWidget(self.check5)
    def checkbox_func(self):
        res = ""
        if self.check1.isChecked():
            res += f"{self.check1.text()}, "
        if self.check2.isChecked():
            res += f"{self.check2.text()}, "
        if self.check3.isChecked():
            res += f"{self.check3.text()}, "
        if self.check4.isChecked():
            res += f"{self.check4.text()}, "
        if self.check5.isChecked():
            res += f"{self.check5.text()} "
        
        self.label3.setText(f"Tanlangan ichimliklar: {res}")
        return res

    def set_radio(self):
        self.r1 = QRadioButton("Naqd")
        self.r1.setStyleSheet(checkbox_style)
        # self.r1.setChecked(True)
        self.r2 = QRadioButton("Karta")
        self.r2.setStyleSheet(checkbox_style)
        self.r3 = QRadioButton("Onlayn")
        self.r3.setStyleSheet(checkbox_style)

        self.vbox.addWidget(self.r1)
        self.vbox.addWidget(self.r2)
        self.vbox.addWidget(self.r3)
      
    def radio_func(self):
        if self.r1.isChecked():
            return self.r1.text()
        elif self.r2.isChecked():
            return self.r2.text()
        else:
            return self.r3.text()

    def show_message(self):
        res = ""
        res += f"Ovqat: {self.combo.currentText()}\n"
        res += f"Ichimliklar: {self.checkbox_func()}\n"
        res += f"To'lov turi: {self.radio_func()}"
        box = QMessageBox()
        box.setStyleSheet(message_style)
        box.setText(res)
        box.exec_()
app = QApplication([])
win = Window()
win.show()
app.exec_()
