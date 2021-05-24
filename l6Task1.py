result_list = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        temp_list = line.split(' ')
        result_list.append((temp_list[0], temp_list[5].replace('"', ''), temp_list[6]))

print(result_list)
