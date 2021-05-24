import re

RE_PARSE_STR = re.compile(r'(^[0-9\.]*|^[a-z0-9\:]*) - - \[([a-z0-9\/:+ ]*)[\] "]*([A-Z]*) ([a-z0-9\/_]*)[A-Z1-9\./" ]*(?<=\" )([0-9]*) ([0-9]*)', re.IGNORECASE)
with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(*map(lambda x: x.group(1, 2, 3, 4, 5, 6), RE_PARSE_STR.finditer(line)), sep=',')