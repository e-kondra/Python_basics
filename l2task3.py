lstr = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(lstr)

for _str in lstr:
    if _str.isdigit():
        print(f'"{int(_str):02d}"', end=' ')
    elif _str[0] == '+' or _str[0] == '-' and _str[1:].isdigit():
        print(f' "{_str[0]}{int(_str[1:]):02d}"', end=' ')
    else:
        print(' ' + _str, end=' ')
