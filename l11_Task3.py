import re

RE_NUM_FL = re.compile(r'\-*\d+\.\d+')
RE_NUM_INT = re.compile(r'\-*\d+')

class MyError(Exception):
    my_list = []

    def __init__(self, text):
        self.text = text

    def input_list(self):
        while True:
            num = input("Введите число :")
            if str(num).upper() == ("stop").upper():
                print(MyError.my_list)
                exit(1)
            try:
                if not RE_NUM_INT.fullmatch(num) and not RE_NUM_FL.fullmatch(num):
                    raise MyError("Value is incorrect and wasn't recorded in list")
            except MyError as err:
                print(err.text)
            else:
                if not RE_NUM_FL.fullmatch(num):
                    num = int(num)
                else:
                    num = float(num)
                MyError.my_list.append(num)


MyError('some words').input_list()
