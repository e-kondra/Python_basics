from functools import wraps

def type_logger(func):

    @wraps(func)
    def type_logger_in(*args, **kwargs):
        print(f'{func.__name__}', end=' ')
        for arg in args:
            print(f'{arg}: {type(arg)}', end=', ')
        a = func(*args)
        print('\nТип значений функции: ', end='')
        for a_ in a:
            print(f'{a_}: {type(a_)}', end=', ')
        print('\nИменованные элементы: ', end='')
        for kw, value in kwargs.items():
            print(f'{kw}: {value}-{type(value)}', end=', ')
    return type_logger_in

@type_logger
def calc_cube(*x, **kwargs):
   return [x_ ** 3 for x_ in x]


calc_cube(2, 0.223, kw1=48, kw2='RUB')
