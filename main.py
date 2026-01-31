import os
os.system("cls")

class Person:
    def __init__(self, i,f,y,m):
        self.ism = i
        self.familya = f
        self.yosh = y
        self.manzil = m
    
    def salomlash(self):
        print(f"Assalom alekum, Men {self.ism}man")

class Employee:
    def __init__(self, i,f,y,m,mo,l):
        self.ism = i
        self.familya = f
        self.yosh = y
        self.manzil = m
        self.lavozim = l
        self.maosh = mo
    
    def salomlash(self):
        print(f"Assalom alekum, Men {self.ism} {self.familya}man. Lavozimim {self.lavozim}")


person1 = Person("Abdulla", "Kadirov", 15, "Toshkent")

employee1 = Employee("Azizbek", "Jalilov", 24, "Namangan", 600, "Menejer")

person1.salomlash()
employee1.salomlash()
