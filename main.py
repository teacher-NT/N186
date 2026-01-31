import os
os.system("cls")

class Car:
    def __init__(self, b,m,r,n,y,s):
        self.brand = b
        self.model = m
        self.rang = r
        self.narx = n
        self.yil = y
        self.soni = s

    def __str__(self):
        return f"{self.brand} {self.model} {self.rang} {self.narx}. {self.soni}ta"
    
    def __eq__(self, n):
        return self.narx == n

    def __ne__(self, n):
        return self.narx != n
    
    def __lt__(self, n):
        return self.yil < n
    
    def __add__(self, n):
        self.narx += n

    def __sub__(self, n):
        self.narx -= n
    
    def __mul__(self, n):
        self.soni *= n
    
    def __truediv__(self, n):
        self.soni //= n

car1 = Car("GM", "Matiz", "OQ", 3000, 2022, 12)

# car1 * 2
car1 / 3

print(car1)        