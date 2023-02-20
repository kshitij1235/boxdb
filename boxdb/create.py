'''
boxdb/auth_boxbd -> v0.9

This file contain code for
1)creating projects and getting details about the project 

made chaneges 
[ ] solved bugs in create_project
'''

from os import chdir, mkdir,listdir
from boxdb.box_encoder import generate_filekey
from boxdb.core import writer
from boxdb.checkups import check_database, check_table
from boxdb.logs import logerror 
from boxdb.tempo_core import add_data,extract_data
from boxdb.settings import TABLE_METADATA,TABLE,COLUMNS_DATA


def get_detail(database,table_name):
    """
    saves meta data of the users
    """
    return extract_data(TABLE_METADATA(database,table_name))

def list_tables(database):
    d=f'./{database}'
    return listdir(d)

def create_database(database_name):
    if(check_database(database_name)):
        logerror(database_name,table=None,message="CREATE : Database or file already exists")
        return False
    mkdir(database_name)

def create_table(database,info):
    """created necessary files in the dir"""

    name=info['name']

    if check_table(database,name,push_error=False):
        logerror(database,None,"CREATE: Project Already Exists")
        return False
        
    try:
        mkdir(TABLE(database,name))
    except Exception as e:
        logerror(database,None,f"CREATE : Cannot create a base directory at {TABLE(database,name)}")
        return False
    
    files = [TABLE_METADATA(database,name), COLUMNS_DATA(database,name)]
    
    dir_=['tables','flags','logs','forbiden']
    
    flag_files = ['./flags/primary_key.txt',
                  './flags/not_null.txt',
                  './flags/unique.txt',
                  './flags/forbidden.txt'
                ]


    for file_ in files:
        generate_filekey(location=f"./{database}/{name}/{name}_key.key")
        if file_ == TABLE_METADATA(database,name):
            writer(file_, " ", "w")
            keys_ = list(info.keys())
            values_ = list(info.values())
            for key, value in zip(keys_, values_):
                add_data(TABLE_METADATA(database,name),key,value)
        else:
            writer(file_,'{ \n }', "w")

    chdir(f"./{database}/{name}")

    for folder in dir_:
        mkdir(folder)
    
    for flags in flag_files:
        writer(flags,"","w")

    chdir("../")
    return True


