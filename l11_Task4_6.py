class MyErr(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def validate_int(num):
        if not num.isdigit():
            raise MyErr("Задано не корректное значение: необходимо целое число")

    @staticmethod
    def validate_num(num):
        try:
            MyErr.validate_int(num)
        except MyErr as err:
            print(err)
            return False
        else:
            return True

    @staticmethod
    def validate_count(num, max_num):
        try:
            MyErr.validate_int(num)
            if int(num) < 1 or int(num) > max_num:
                raise MyErr(f'Число не корректное, необходимо от 1 до {max_num}')
        except MyErr as err:
            print(err)
            return False
        else:
            return True


class Stock:
    tech_in_stock = {
        'Printer': {'Epson L386': 2, 'HP Ink Tank 115': 1, 'HP LaserJet Pro M404dw': 12, 'HP LaserJet Pro 107a': 4},
        'Scanner': {'Epson Perfection V19': 1},
        'Copier': {'Xerox WorkCentre 7232/7242': 1}
    }

    parts = ['Head', 'IT', 'Buch', 'Sale', 'Personal']

    tech_in_parts = {
        'Buch': {'Printer Epson L386': 1}
    }

    def __init__(self):
        pass

    @classmethod
    def accept(cls, name, brand, model, count):
        in_stock = cls.tech_in_stock.get(name)
        if in_stock.get(f'{brand} {model}'):
            in_stock[f'{brand} {model}'] += count
        else:
            in_stock[f'{brand} {model}'] = count
        # print(cls.tech_in_stock)

    @classmethod
    def transfer(cls, part, name, brand, model, count):
        items = {}
        in_part = cls.tech_in_parts.get(part)
        if not in_part:
            items[f'{name} {brand} {model}'] = count
            cls.tech_in_parts[part] = items
        else:
            if in_part.get(f'{name} {brand} {model}'):
                in_part[f'{name} {brand} {model}'] += count
            else:
                in_part[f'{name} {brand} {model}'] = count
        cls.tech_in_stock.get(name)[f'{brand} {model}'] -= count
        if cls.tech_in_stock.get(name)[f'{brand} {model}'] == 0:
            items = cls.tech_in_stock.get(name)
            del (items[f'{brand} {model}'])

    @classmethod
    def print_stock(cls):
        for key, val in cls.tech_in_stock.items():
            print(f"{key}:")
            for key_, val_ in val.items():
                print(f"\t{key_} - {val_} шт.")

    @classmethod
    def print_parts(cls):
        for key, val in cls.tech_in_parts.items():
            print(f"{key}:")
            for key_, val_ in val.items():
                print(f"\t{key_} - {val_} шт.")


class OfficeEquipment:
    def __init__(self, name, brand, model):
        self.name = name
        self.brand = brand
        self.model = model


class Printer(OfficeEquipment):
    def __init__(self, brand, model, typ='laser', color=False):
        super().__init__('Printer', brand, model)
        self.color = color
        self.typ = typ

    @classmethod
    def set_printer(cls):
        brand = input("Укажите бренд: ")
        model = input("Укажите модель: ")
        typ = input("Укажите тип печати 1 - laser, 2 - jet): ")
        color = input("1 - Цветной, 2 - ч/б (0): ")
        return cls(brand, model, 'jet' if int(typ) == 1 else None, True if int(color) == 1 else False)

    def __str__(self):
        return f"{self.name} {self.brand} {self.model} {self.typ} {'color' if self.color == True else 'black/white'}"


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, typ='planshet'):
        super().__init__('Scanner', brand, model)
        self.typ = typ

    def __str__(self):
        return f"{self.name} {self.brand} {self.model} {self.typ}"

    @classmethod
    def set_scaner(cls):
        brand = input("Укажите бренд: ")
        model = input("Укажите модель: ")
        typ = input("Тип: планшетный - 1, протяжный - 2: ")
        return cls(brand, model, 'broaching' if int(typ) == 2 else None)


class Copier(OfficeEquipment):
    def __init__(self, brand, model):
        super().__init__('Copier', brand, model)

    def __str__(self):
        return f"{self.name} {self.brand} {self.model}"

    @classmethod
    def set_copier(cls):
        brand = input("Укажите бренд: ")
        model = input("Укажите модель: ")
        return cls(brand, model)


st = Stock()
while True:
    print('Какое действие Вы хотите выполнить?\n1 - Принять оргтехнику на склад\n2 - Переместить в подразделение\n3 - '
          'Просмотреть состояние склада\n4 - Просмотреть наличие оргтехники в подразделениях\n5 - Выход из программы')
    n = input("Введите цифру :")
    if not MyErr.validate_num(n):
        continue
    if int(n) == 5:
        exit(1)
    elif int(n) == 1:  # Принять на склад
        print("Какую оргтехнику Вы хотите принять: \n1 - Принтер\n2 - Сканер\n3 - Копировальное устройство")
        a = input("Введите цифру : ")
        if not MyErr.validate_num(a):
            continue
        count = input("Введите количество : ")
        if not MyErr.validate_num(count):
            continue
        if int(a) == 1:
            pr = Printer.set_printer()
            Stock.accept(pr.name, pr.brand, pr.model, int(count))
        elif int(a) == 2:
            scan = Scanner.set_scaner()
            Stock.accept(scan.name, scan.brand, scan.model, int(count))
        elif int(a) == 3:
            cp = Copier.set_copier()
            Stock.accept(cp.name, cp.brand, cp.model, int(count))
        print('Принято успешно')
    elif int(n) == 2:  # Переместить в подразделение
        print("Выберите подразделение:")
        for i in range(len(Stock.parts)):
            print(f"{i + 1} - {Stock.parts[i]}")
        podr = input("Укажите номер подразделения: ")
        while not MyErr.validate_num(podr):
            podr = input("Укажите номер подразделения: ")
        podr = Stock.parts[int(podr) - 1]
        print("Какую оргтехнику Вы хотите переместить: \n1 - Принтер\n2 - Сканер\n3 - Копировальное устройство")
        a = input("Введите цифру :")
        while not MyErr.validate_num(a):
            a = input("Введите цифру :")
        print("Выберите доступный вариант: ")
        tech = 'Printer' if int(a) == 1 else ('Scanner' if int(a) == 2 else 'Copier')
        idx = 0
        idx_ = 0
        val = st.tech_in_stock.get(tech).copy()
        if val:
            for key_, val_ in val.items():
                idx += 1
                print(f"{idx}.{key_} - {val_} шт")
            b = input("Введите цифру :")
            while not MyErr.validate_num(b):
                b = input("Введите цифру :")
            for key_, val_ in val.items():
                idx_ += 1
                if idx_ == int(b):
                    br = key_[:key_.find(' ')]
                    mod = key_[key_.find(' ') + 1:]
                    count = input(f"Введите количество от 1 до {val_}: ")
                    while not MyErr.validate_count(count, val_):
                        count = input(f"Введите количество от 1 до {val_}: ")
                    st.transfer(podr, tech, br, mod, int(count))
                    print(f'{tech} успешно перемещен/-ы в подразделение {podr}')
        else:
            print(f'Внимание! На складе нет доступной оргтехники типа {tech}. Выберите другое действие')
    elif int(n) == 3:
        Stock.print_stock()
    elif int(n) == 4:
        Stock.print_parts()
