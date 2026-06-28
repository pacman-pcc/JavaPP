# libs/POS.py

import os

def get_cd_user(new_path):
    return os.chdir(new_path)

def create_mkdir(mkdir_path):
    return os.mkdir(mkdir_path)

def create_makefullfolder(mkfull_path):
    return os.makedirs(mkfull_path)

def ls_dir(ls_path):
    return os.listdir(ls_path)

def remove_file(del_path):
    return os.remove(del_path)

def rename_file(r_src, dst):
    return os.rename(r_src, dst)

def cwd_me():
    return os.getcwd()

def walk_style(walk_path):
    return list(os.walk(walk_path))

def system_pos(command):
    return os.system(command)

def pos_name():
    return os.name

# Connecting
LIB_FUNCS["change.directory"] = get_cd_user
LIB_FUNCS["create.makedirectory"] = create_mkdir
LIB_FUNCS["create.fullydirectory"] = create_makefullfolder
LIB_FUNCS["ls.in"] = ls_dir
LIB_FUNCS["delete.in.terminate"] = remove_file
LIB_FUNCS["rename.file"] = rename_file
LIB_FUNCS["oh.my.cwd"] = cwd_me
LIB_FUNCS["walk.in"] = walk_style
LIB_FUNCS["ready.system.console.text"] = system_pos
LIB_FUNCS["pos.name.os"] = pos_name
