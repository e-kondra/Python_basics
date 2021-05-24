class MyDevisionErr(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def division(a, b):
        try:
            if b == 0:
                raise MyDevisionErr('Деление на ноль невозможно')
        except MyDevisionErr as err:
            return err
        else:
            return a / b


print(MyDevisionErr.division(45, 0))