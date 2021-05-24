from abc import ABC, abstractmethod

class Cloth(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def textile_consump(self):
        pass

class Coat(Cloth):
    def __init__(self, size):
        self.size = size
        super().__init__('пальто')

    @property
    def textile_consump(self):
        return round(self.size/6.5 + 0.5, 2)

class Costume(Cloth):
    def __init__(self, height):
        self.height = height
        super().__init__('костюм')

    @property
    def textile_consump(self):
        return round(2 * self.height + 0.3, 2)

def full_consump(num1, num2):
    return Coat(num1).textile_consump + Costume(num2).textile_consump

coat = Coat(42)
print(coat.textile_consump)
costum = Costume(1.7)
print(costum.textile_consump)
print(full_consump(42, 1.7))