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

    def __gt__(self, n):
        if isinstance(n, int):
            return self.yosh > n
        elif isinstance(n, Employee):
            return self.yosh > n.yosh
        else:
            return f"TypeError: {type(n)} mumkin emas."

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
    
    def __gt__(self, n):
        return self.maosh > n


person1 = Person("Abdulla", "Kadirov", 15, "Toshkent")

employee1 = Employee("Azizbek", "Jalilov", 12, "Namangan", 600, "Menejer")

print(person1 > employee1)
print(person1 > 18)
print(person1 > 22.5)
# print(employee1 > 300)



# person1.salomlash()
# employee1.salomlash()
