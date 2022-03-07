from os.path import join
from os import makedirs

main_dir = "my_project"
sub_dir = "setting", "mainapp", "adminapp", "authapp"
for n in sub_dir:
    path = join(".", main_dir, n)
    makedirs(path, exist_ok=True)