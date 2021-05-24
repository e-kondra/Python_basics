my_dict = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.split(' ')[0] in my_dict:
            my_dict[line.split(' ')[0]] += 1
        else:
            my_dict.setdefault(line.split(' ')[0], 1)

print(*(i for i in my_dict if my_dict[i] == max(my_dict.values())), ', запросов', max(my_dict.values()))
