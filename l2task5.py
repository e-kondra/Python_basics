price = [2.37, 14, 16.03, 149.8, 3.03, 5.9, 97, 13.18, 6.55, 11.11, 6, 45.63]
# A
for cost in price:
    print(f'{int(float(cost) // 1)} руб.{int(cost % 1 * 100 + 0.005) : 03d} коп.', end=', ')
# B
print(f'\nLists id before sort: {id(price)}')
price.sort()
print(f'Sorted list : {price}')
print(f'Lists id after sort: {id(price)}')
# C
price_2 = sorted(price, reverse=True)
print(f'New list reversed: {price_2}')

# D
print('The 5 most expensive items:')
for i in range(0, 5):
    print(price_2[i], end=', ')

print('\nThe 5 most expensive items in ascending order:')
for i in range(4, -1, -1):
    print(price_2[i], end=', ')
print('\n or ')
print(list(reversed(price_2[0:5])))
