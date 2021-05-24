class Iterator:
    def __init__(self, step, stop, start=1):
        self.i = start - 1
        self.step = step
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        self.i += self.step
        if self.i <= self.stop:
            return f'{"*" * self.step}'
        else:
            raise StopIteration

class Cell:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number)

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number - other.number > 0:
            return Cell(self.number - other.number)
        else:
            raise('Невозможно выполнить вычитание')

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __floordiv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, num_in_row):
        """такое решение только для того чтобы опробовать новый материал"""
        iter = Iterator(num_in_row, self.number)
        for i in iter:
            print(i)
        print(f'{"*" * int(self.number % num_in_row)}')

cell_1 = Cell(10)
cell_2 = Cell(3)
cell_3 = cell_1 + cell_2
cell_4 = cell_1 - cell_2
print(cell_3)
print(cell_4.number)
print(cell_4 * cell_3)
print(cell_4 * cell_3 // cell_1 + cell_2)
print()
cell_1.make_order(4)
