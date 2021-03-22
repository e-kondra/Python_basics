class Stationery:
    def __init__(self, title='stationery'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")

class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом")

class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером")


St = Stationery()
St.draw()
p = Pen()
p.draw()
pnc = Pencil()
pnc.draw()
hnd = Handle()
hnd.draw()
