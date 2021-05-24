import re

RE_COMPLEX = re.compile(r'([-]?\d*\.*\d*)?([+|-]?\d*\.*\d+[j]{1})$')
RE_IMAG = re.compile(r'^[+|-]?\d*\.*\d+[j]{1}$')

class MyError(Exception):
    def __init__(self, text):
        self.text = text

class MyComplexNum:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @classmethod
    def set_num(cls, num_txt):
        num_txt = num_txt.replace(' ', '')
        try:
            if num_txt.find('+') > 0 or num_txt.rfind('-') != -1:
                if RE_COMPLEX.finditer(num_txt):
                    a = list(*map(lambda x: x.group(1, 2), RE_COMPLEX.finditer(num_txt)))
                    r, i = a
            elif RE_IMAG.fullmatch(num_txt):
                r = 0
                i = num_txt
            else:
                raise MyError('Incorrect value')
        except MyError as err:
            print(err)
        else:
            return cls(float(r), float(i.replace('j', '')))

    def __str__(self):
        return str(f'{self.real}{"+" if float(self.imag) > 0 else ""}{self.imag}j')

    def __add__(self, other):
        a1 = self.real + other.real
        a2 = self.imag + other.imag
        return MyComplexNum.set_num(f'{a1}{"+" if float(a2) > 0 else ""}{a2}j')

    def __mul__(self, other):
        m1 = round(self.real * other.real - self.imag * other.imag, 2)
        m2 = round(other.real * self.imag + self.real * other.imag, 2)
        return MyComplexNum.set_num(f'{m1}{"+" if float(m2) > 0 else ""}{m2}j')


a = MyComplexNum.set_num('3+0.2j')
b = MyComplexNum.set_num('3.0j')
c = MyComplexNum.set_num('-2-12j')
print(a)
print(b)
print(c)
print(a + b + c)
print(a * b * c)
