def nums_generator(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


n = 21
nums_gen = nums_generator(n)

for n in range(1, n + 1, 2):
    print(next(nums_gen), end=', ')
print('\n')

# 2-й вариант для задания №2

print(*(num for num in range(1, n + 1, 2)))
