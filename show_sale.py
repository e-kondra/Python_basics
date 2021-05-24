import sys

n = 0
f = open('bakery.csv', 'r', encoding='utf-8')
if len(sys.argv) == 1:
    for line in f:
        print(line, end='')
elif len(sys.argv) == 2:
    data = sys.argv[1]
    a = f.readlines()[int(data)-1:]
    for item in a:
        print(item, end='')
else:
    data = sys.argv[1]
    end = sys.argv[2]
    a = f.readlines()[int(data) - 1:int(end)]
    for item in a:
        print(item, end='')
