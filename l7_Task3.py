import os
import shutil

my_proj = r'C:\Users\User\PycharmProjects\Python_basics\l7_Tasks\my_project'
templates_dir = os.path.join(my_proj, 'templates')

if not os.path.exists(templates_dir):
    os.mkdir(templates_dir)
for main_dir in os.listdir(my_proj):
    templs = [d for d in os.scandir(os.path.join(my_proj, main_dir)) if d.name == 'templates']
    for r in templs:
        r_dir = os.path.join(templates_dir, main_dir)
        if not os.path.exists(r_dir):
            os.mkdir(r_dir)
        for root, dir, file in os.walk(r):
            for f in os.scandir(root):
                if f.is_file():
                    shutil.copyfile(f.path, os.path.join(r_dir, f.name))
