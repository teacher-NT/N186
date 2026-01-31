import os
os.system("cls")

class Car:
    def __init__(self, b,m,r,n,y):
        self.brand = b
        self.model = m
        self.rang = r
        self.narx = n
        self.yil = y

    def __str__(self):
        return f"{self.brand} {self.model} {self.rang} {self.narx}"
    
    def __eq__(self, n):
        return self.narx == n

    def __ne__(self, n):
        return self.narx != n
    
    def __lt__(self, n):
        return self.yil < n

car1 = Car("GM", "Matiz", "OQ", 3000, 2022)
print(car1 == 2000)
print(car1 != 2000)
print(car1 < 2020)

print(car1)        