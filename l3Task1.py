from random import choice

num_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять'
}


def num_translate(number):
    return num_dict[number]


print(num_translate(choice(list(num_dict.keys()))))
