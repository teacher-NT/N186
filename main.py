import os
os.system("cls")

from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def jump(self):
        pass

    @abstractmethod
    def kick(self):
        pass


class General(Player):
    def __init__(self, n,s):
        self.nickname = n
        self.s = s
    def run(self):
        print(f"{self.nickname} is running...")

    def kick(self):
        print(f"{self.nickname} is kicking...")

    def jump(self):
        print(f"{self.nickname} is jumping...")
        
general1 = General("Spiderman", 1000)
