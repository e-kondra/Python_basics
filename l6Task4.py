f1 = open('users.csv', 'r', encoding='utf-8')
f2 = open('hobby.csv', 'r', encoding='utf-8')
f_res = open('users_hobby.csv', 'w', encoding='utf-8')

user = 1
hobby = 1
while user or hobby:
    user = f1.readline().strip().replace(',', ' ')
    hobby = f2.readline().strip()
    if user or hobby:
        f_res.write(f"{user if user else None} : {hobby if hobby else None}\n")


