import sys

data = sys.argv[1].replace(',', '.')

f = open('bakery.csv', 'a', encoding='utf-8')
f.write(f'{data}\n')
f.close()
