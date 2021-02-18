my_list = []
full_summ = 0
# a.
for i in range(1, 1000, 2):
    my_list.append(i ** 3)

for i in my_list:
    num = i
    sum_num = 0
    while num > 0:
        sum_num += num % 10
        num //= 10
    if sum_num % 7 == 0:
        full_summ += i
print('a.', full_summ)

# b
full_summ = 0
my_second_list = []
for i in my_list:
    my_second_list.append(i + 17)

for i in my_second_list:
    num = i
    sum_num = 0
    while num > 0:
        sum_num += num % 10
        num //= 10
    if sum_num % 7 == 0:
        full_summ += i
print('b.', full_summ)

# c Решить задачу под пунктом b, не создавая новый список
full_summ = 0
for i in my_list:
    num = i + 17
    sum_num = 0
    while num: # хотела спросить почему так тоже работает? потому что False = 0?
        sum_num += num % 10
        num //= 10
    if sum_num % 7 == 0:
        full_summ += i + 17
print('c.', full_summ)