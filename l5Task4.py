def get_new_list(src_):
    n = src_[0]
    for num in src_:
        if num > n:
            yield num
        n = num


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = get_new_list(src)

print(*new_list, sep=', ')
