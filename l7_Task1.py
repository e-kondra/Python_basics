import os

root = "my_project"
folds = ["settings", "mainapp", "adminapp", "authapp"]

if not os.path.exists(root):
    os.mkdir(root)

res_folds = [os.mkdir(os.path.join(root, fold))
             for fold in folds if not os.path.exists(os.path.join(root, fold))]


