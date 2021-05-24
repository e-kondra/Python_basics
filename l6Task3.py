import json
f1 = open('users.csv', 'r', encoding='utf-8')
f2 = open('hobby.csv', 'r', encoding='utf-8')
l1 = list(map(lambda el: el.replace(',', ' '), f1.readlines()))
l2 = f2.readlines()

comb_dict = {l1[n].replace('\n', ''): (l2[n].replace('\n', '') if n < len(l2) else None) for n in range(0, len(l1))}

f1.close()
f2.close()

with open('result_file.json', 'w', encoding='utf-8') as js_f:
    js_f.write(json.dumps(comb_dict, ensure_ascii=False, indent=0))

# Это десериализация, для проверки
#with open('result_file.json', 'r', encoding='utf-8') as f:
#    dict_as_str2 = f.read()
#new_dict = json.loads(dict_as_str2)
#print(new_dict, type(new_dict))


