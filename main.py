import os
os.system("cls")
import random as rd
from PyQt5.QtWidgets import ( 
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit
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


app = QApplication([])

oyna = QWidget()
oyna.setWindowTitle("Mening birinchi dasturim")
oyna.setGeometry(1350,200, 400,700)
oyna.setStyleSheet("background-color:#303670;")

label1 = QLabel(oyna)
label1.setText("Qani boshladik")
label1.move(100, 20)
label1.setStyleSheet("font-size:30px; color:#ffffff;")

inpt = QLineEdit(oyna)
inpt.setGeometry(50,100, 300, 50)
inpt.setStyleSheet(input_style)
inpt.setPlaceholderText("Davlat nomini kiriting...")

label2 = QLabel(oyna)
label2.setFixedWidth(150)
label2.move(80, 180)
label2.setStyleSheet("font-size:30px; color:#ffffff;")

def func_btn1():
    capitals = {
        "O'zbekiston": "Toshkent",
        "Rossiya": "Moskva",
        "Qozog'iston": "Astana",
        "Angliya":"London",
        "Ispaniya": "Madrid",
        "Italiya": "Rim",
        "Germaniya": "Berlin",
        "Fransiya": "Parij",
        "Turkiya": "Anqara",
        "Misr": "Qohira",
        "Yaponiya": "Tokio"
    }
    text = inpt.text()
    if text in capitals:
        n = capitals[text]
        label2.setText(n)
    else:
        print("Ma'lumot topilmadi🤔")

    
btn1 = QPushButton(oyna)
btn1.setText("🔍Search")
btn1.setStyleSheet(btn_style)
btn1.setGeometry(115,325, 170, 50)
btn1.clicked.connect(func_btn1)


oyna.show()
app.exec_()
