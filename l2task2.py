lstr = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print (lstr)
new_lstr = []

for _str in lstr:
    if _str.isdigit():
        new_lstr.append(f'"{int(_str):02d}"')
    elif _str[0] == '+' or _str[0] == '-' and _str[1:].isdigit():
        new_lstr.append(f'"{_str[0]}{int(_str[1:]):02d}"')
    else:
        new_lstr.append(_str)

_str2 = ' '.join(new_lstr)
print(_str2)