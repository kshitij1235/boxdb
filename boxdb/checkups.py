"""
boxdb/table_checkup.py -> v0.9

This file contain code for
1)to check table

[ ] internal check primary row fixed
"""
from os import path,stat

from os.path import exists

from boxdb.core import word_find

from boxdb.support import(
    get_columns_datatype,
    get_elements,
    get_primary_column,
    get_columns)

from boxdb.settings import TABLE,COLUMNS

from boxdb.logs import logWarning,logerror

def check_table(database,table_name,push_error=True):
    """
    checks if table exist's or not
    """
    path_condition = bool(path.exists(TABLE(database,table_name)))
    if not path_condition and push_error is True:
        logerror(database=database,table=None,message="CHECKUP : TABLE NOT FOUND")
    return path_condition
    
def check_database(database):
    """
    checks if table exist's or not
    """
    return bool(path.exists(f'./{database}'))

def column_exists(database,table_name,column):
    """
    Checks column exists in file system
    """
    return exists(COLUMNS(database,table_name,column))

def row_element_exist(database,table_name,column,element):
    """
    check if the element exist in column
    """
    return word_find(COLUMNS(database,table_name,column), element)


def primary_key_exists(database,table_name):
    primary_key=get_primary_column(database,table_name)
    if primary_key is None:
        logerror(database,table_name,f"PRIMARY KEY : does not exists in {table_name}")
        return False
    return primary_key

def empty_table(database,table_name):
    """
    check weather the table is empty or not
    """
    columns=get_columns(database,table_name)
    flags = [stat(COLUMNS(database,table_name,column)).st_size for column in columns]
    if flags.count(False) != len(columns):
        return True
    logerror(database,table_name,"TABLE : table is empty")
    return False

def check_priamary_column(database,table_name,primary_key):
    """
    Checks where there is problem in primary key
    """
    # get primary column 
    primary_elements=get_elements(database,table_name,primary_key)
    if ['null','',' '] in primary_elements:
        return False
    temp= set(primary_elements)
    return len(primary_elements) == len(temp)

def table_struture_exists(database,table_name):
    """
    checks if table structure exits
    """
    content=get_columns(database,table_name)
    if not content:
        logWarning(database,table_name, f"TABLE : {table_name} has no structure yet")
        return False
    return True

def check_datatypes(database,table_name,data):

    columns_datatype=get_columns_datatype(database,table_name)
    
    for column_datatype , element in zip(columns_datatype,data):
        if column_datatype == "str" and not isinstance(element, str):
            logerror(database,table_name,f"CHECKUP: DataType string required for {element}")
            return False
        if column_datatype == "int" and not isinstance(element, int):
            logerror(database,table_name,f"CHECKUP: DataType int required for {element}")
            return False
        if column_datatype == "bool" and not isinstance(element, bool):
            logerror(database,table_name,f"CHECKUP: DataType int required for {element}")
            return False
    return True

def checkup_table_struct(database,table_name):
    """
    perform a combo of checks
    """
    if not check_table(database,table_name):
        return False

    # check if table is empty or not
    if not empty_table(database,table_name):
        return False
        
    return True