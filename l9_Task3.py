inc = {'wage': 50000, 'bonus': 12000}

class Worker:

    def __init__(self, name, surname, position, inc_=inc):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = inc_

class Position(Worker):
    def get_full_name(self):
        return(f'{self.name} {self.surname}')

    def get_total_income(self):
        return(f"{self._income['wage'] + self._income['bonus']} руб.")



man = Position('Сергей', 'Колосков', 'менеджер')
print(man.position, man.name, man.surname, sep=',')
print(man.get_full_name(), man.get_total_income())

inc2 = {'wage': 60000, 'bonus': 11000}
man2 = Position('Петр', 'Захаров', 'механик', inc2)

print(man2.get_full_name(), man2.get_total_income())




