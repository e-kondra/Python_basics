class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self, l, w, m_m=5, h=1):
        return l * w * m_m * h / 1000


r = Road(20, 4000)
print(f'{r.calc_mass(r._length, r._width, 25, 5)} т.')
print(f'{r.calc_mass(r._length, r._width)} т.')
