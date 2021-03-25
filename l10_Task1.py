class Matrix:
    def __init__(self, spis):
        self.spis = spis

    def __str__(self):
        temp_str = ''
        for i in self.spis:
            for n in i:
                temp_str += f' {str(n)}'
            temp_str += f'\n'
        return temp_str

    def __add__(self, other):
        return Matrix([
            [cell_1 + cell_2 for cell_1, cell_2 in zip(row_1, row_2)]
            for row_1, row_2 in zip(self.spis, other.spis)
        ])


matx1 = Matrix([[1, 2, 3], [3, 4, 5], [4, 3, 2]])
matx2 = Matrix([[2, 2, 2], [3, 4, 5], [4, 4, 4]])
matx3 = Matrix([[1, 2, 1], [1, 4, 1], [1, 4, 1]])
print(matx1)
print(matx2)
print(matx1 + matx2 + matx3)