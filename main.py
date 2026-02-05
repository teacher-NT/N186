import os
os.system("cls")
import random as rd
from PyQt5.QtWidgets import ( 
    QApplication, QWidget, QLabel,
    QPushButton
)

btn_style = """
    background-color:#e8e689;
    color:black;
    font-size:20px;
    border-radius:20px;
    border: 2px solid red;
"""

app = QApplication([])

oyna = QWidget()
oyna.setWindowTitle("Mening birinchi dasturim")
oyna.setGeometry(1350,200, 400,700)
oyna.setStyleSheet("background-color:#303670;")

label1 = QLabel(oyna)
label1.setText("Bizning dasturdan salom!")
label1.setStyleSheet("font-size:30px; color:#ffffff;")

def func_btn1():
    label1.setText("Ilova tugmasi bosildi...")
    colors = ["red", "green", "blue", "yellow", "white", "purple"]
    color = rd.choice(colors)
    oyna.setStyleSheet(f"background-color:{color};")
btn1 = QPushButton(oyna)
btn1.setText("Tugmani bosing")
btn1.setStyleSheet(btn_style)
btn1.setGeometry(115,325, 170, 50)
btn1.clicked.connect(func_btn1)

oyna.show()
app.exec_()
