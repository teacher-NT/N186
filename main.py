import os
os.system("cls")

class Car:
    def __init__(self, b,m,r,n,y,s):
        self.brand = b
        self.model = m
        self.ranglar = r
        self.narx = n
        self.yil = y
        self.soni = s

    def __str__(self):
        return f"{self.brand} {self.model} {self.ranglar} {self.narx}. {self.soni}ta"
    
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

    def __len__(self):
        return  len(self.ranglar)
    
    def __contains__(self, n):
        n = n.lower()
        i = 0
        while i < len(car1):
            if self.ranglar[i].lower() == n:
                return True
            i += 1
        return False
        # if n in self.ranglar:
        #     return True
        # else:
        #     return False

    

car1 = Car("GM", "Matiz", ['Oq', 'Qora', 'Qizil', 'YAshiL', "Ko'k"], 3000, 2022, 12)

# print(len(car1))
if "yashil" in car1:
    print("Yes")
else:
    print("No")

print(car1)        