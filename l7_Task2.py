import yaml
import os

def make_dir_str(a,b):
    if not os.path.exists(os.path.join(a, b)):
        if '.' in b:
            file = open(os.path.join(a, b), 'w', encoding='utf-8')
            file.close()
        else:
            return os.mkdir(os.path.join(a, b))

def make_dir_list(dir, list_):
    for f in list_:
        if type(f) == str:
            make_dir_str(dir, f)
        elif type(f) == dict:
            make_dir_dict(dir, f)


def make_dir_dict(a, dic):
    for key, val in dic.items():
        make_dir_str(a, key)
        if type(val) == list:
            make_dir_list(os.path.join(a, key), val)
        elif type(val) == str:
            make_dir_str(os.path.join(a, key), val)
        elif type(val) == dict:
            make_dir_dict(key, val)

with open('config.yaml') as f:
    templates = yaml.safe_load(f)

print(templates)
make_dir_dict('', templates)
