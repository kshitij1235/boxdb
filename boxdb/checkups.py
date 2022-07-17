"""
boxdb/table_checkup.py -> v0.9

This file contain code for
1)to check table

[ ] internal check primary row fixed
"""
from os import path,stat
from os.path import exists
from filemod import word_find
from boxdb.support import(
    get_elements,
    get_primary_column,
    get_columns)

from boxdb.logs import logWarning,logerror

def check_table(table_name):
    """
    checks if table exist's or not
    """
    return bool(path.exists(f"./{table_name}"))

def column_exists(table_name,column):
    """
    Checks column exists in file system
    """
    return exists(f"./{table_name}/tables/{column}.txt")

def row_element_exist(table_name,column,element):
    """
    check if the element exist in column
    """
    return word_find(f"./{table_name}/tables/{column}.txt", element)


def primary_key_exists(table_name):
    primary_key=get_primary_column(table_name)
    if primary_key is []:
        logerror(table_name,f"PRIMARY KEY : does not exists in {table_name}")
        return False
    return primary_key

def empty_table(table_name):
    """
    check weather the table is empty or not
    """
    columns=get_columns(table_name)
    flags = [stat(f'./plasma/tables/{column}.txt').st_size for column in columns]
    if flags.count(False) != len(columns):
        return True
    print("TABLE : table is empty")
    return False

def check_priamary_column(table_name,primary_key):
    """
    Checks where there is problem in primary key
    """
    # get primary column 
    primary_elements=get_elements(table_name,primary_key)
    if ['null','',' '] in primary_elements:
        return False
    temp= set(primary_elements)
    return len(primary_elements) == len(temp)

def table_struture_exists(table_name):
    """
    checks if table structure exits
    """
    content=get_columns(table_name)
    if not content:
        logWarning(table_name, f"TABLE : {table_name} has no structure yet")
        return False
    return True
