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

reset_style = """
    background-color:red;
    color:black;
    font-size:20px;
    border-radius:20px;
    border: 2px solid blue;
"""

count_style = """
    font-size:60px;
    color: black;
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

count_label = QLabel(oyna)
count_label.setText("0")
count_label.move(180,100)
count_label.setFixedWidth(100)
count_label.setStyleSheet(count_style)

count = 0
def func_btn1():
    global count
    count += 1
    # colors = ["red", "green", "blue", "yellow", "white", "purple"]
    # color = rd.choice(colors)
    # oyna.setStyleSheet(f"background-color:{color};")
    count_label.setText(str(count))

btn1 = QPushButton(oyna)
btn1.setText("Count")
btn1.setStyleSheet(btn_style)
btn1.setGeometry(115,325, 170, 50)
btn1.clicked.connect(func_btn1)

def reset_func():
    global count
    count = 0
    count_label.setText(str(count))

reset_btn = QPushButton(oyna)
reset_btn.setText("Reset")
reset_btn.setStyleSheet(reset_style)
reset_btn.setGeometry(115,380, 170, 50)
reset_btn.clicked.connect(reset_func)

oyna.show()
app.exec_()
