slist = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for emp in slist:
    print(f'Привет, {emp[emp.rfind(" ") + 1:].capitalize()}!')
