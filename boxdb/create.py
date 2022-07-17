'''
boxdb/auth_boxbd -> v0.9

This file contain code for
1)creating projects and getting details about the project 

made chaneges 
[ ] solved bugs in create_project
'''

from filemod import reader, writer
from boxdb.checkups import check_table
from os import mkdir, chdir

def get_detail(table_name):
    """
    saves meta data of the users
    """
    return reader(f"./{table_name}/{table_name}_meta.txt")


def create_project(info):
    """created necessary files in the dir"""

    #FIXME add a extra file structure
    #flags/not_null.txt and primary_key.txt

    name=info['name']

    if check_table(name):
        print("project already exists")
        return False
        
    try:
        mkdir(name)
    except Exception:
        return False
    

    writing=''
    keys_ = list(info.keys())
    values_ = list(info.values())
    for key, value in zip(keys_, values_):
        writing = f"{writing} {key}:{value}\n"

    files = [f"./{name}/{name}_meta.txt", f"./{name}/{name}_data.txt"]
    
    dir_=['tables','flags','logs','forbiden']
    
    flag_files = ['./flags/primary_key.txt',
                  './flags/not_null.txt',
                  './flags/unique.txt',
                  './flags/forbidden.txt'
                ]


    for file_ in files:
        if file_ == f"./{name}/{name}_meta.txt":
            writer(file_, writing, "w")
        else:
            writer(file_,'', "w")

    chdir(f"./{name}")

    for folder in dir_:
        mkdir(folder)
    
    for flags in flag_files:
        writer(flags,"","w")

    chdir("../")


    return True
