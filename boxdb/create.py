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
from boxdb.checkups import check_database, check_table,column_exists
from boxdb.logs import logerror 
from boxdb.tempo_core import add_data,extract_data
from boxdb.support import write_dict
from boxdb.settings import TABLE_METADATA,TABLE,COLUMNS_DATA,DATABASE_TABLE

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
    Meta_data={"name":database_name,"tables":"0"}
    
    mkdir(database_name)
    writer(f"./{database_name}/{database_name}_META.txt","{ \n","+w")

    for keys , values in zip(Meta_data.keys(),Meta_data.values()):
        writer(f"./{database_name}/{database_name}_META.txt",f"{keys} : {values} \n ","a")
    
    writer(f"./{database_name}/{database_name}_META.txt","}","a")

    writer(f"./{database_name}/{database_name}_TABLE.txt","{\n","+w")
    writer(f"./{database_name}/{database_name}_TABLE.txt","}","a")

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
    chdir("../")

    add_data(DATABASE_TABLE(database),name,"0")
    
    return True


def create_view(database,view_name,column_data):
    if check_database(database):
        tables=column_data.values()
        columns=column_data.keys()       
        for table in tables:
            if not check_table(database,table,push_error=False):
                logerror(database,None,f"CREATE : Table {table} does not exists for view")
                return False

        for table , column in zip(tables,columns):
            if not column_exists(database,table,column):
                logerror(database,None,f"CREATE : Column {column} does not exist in table {table} for view")


        write_dict(f"./{database}/{view_name}.txt",column_data.keys(),column_data.values())
    else:
        logerror(database,None,"CREATE : database does not exsits")