'''
boxdb/basic_commands -> v1.0

This file contain code for
1)row,column creation and deletion
2)and gettting table

get_table() -> Added word buffer
'''

import asyncio
from boxdb.core import writer
from tabulate import tabulate
from boxdb.settings import PRIMARY_KEY
from boxdb.readtable import row_table,row__multiple_table
from boxdb.support import (get_primary_column,
get_columns,
AddFlagsToColumns,
get_view_column,
get_view_table )

from boxdb.checkups import (column_exists,
primary_key_exists,
check_priamary_column,
check_table)

from boxdb.FileWriteup import write_element_in_primary
from boxdb.logs import logWarning, loginfo, logerror


#TODO row_limit need to be implemented

def get_table(database,
table_name,
data=None,
columns=None,
Display=True,
index='always',
style="texttile",
row_limiit=None,
word_buffer=None
):
    """
    It is used to display table in terminal or even filture
    out some rows according to the convience
    """
    
    if data is not None :
        columns= get_columns(database,table_name)
        return tabulate(data, headers=columns, showindex=index, tablefmt=style)

    if columns is None:
        columns= get_columns(database,table_name)
    lazy_data=asyncio.run(row_table(database,table_name,columns,limit_row=row_limiit,word_buffer=word_buffer))

    #LAZY_DATA is false when no data in table
    if lazy_data is False:
        return False
    
    if not Display: 
        return lazy_data

    processed = AddFlagsToColumns(database,table_name, columns)
    
    return tabulate(lazy_data, headers=processed, showindex=index, tablefmt=style)

def display_data(data,
database=None,
table_name=None,
columns=None,
index='always',
style="texttile",
):
    """
    It is used to print data 
    """
    columns=[]
    if data is not None:
        if database and table_name is not None:
            columns= get_columns(database,table_name)
        else:
            columns = [f"columns_{i}" for i in range(len(data[0]))]
        return tabulate(data, headers=columns, showindex=index, tablefmt=style)

def get_view(database,
view_name,
index='always',
style="texttile",
row_limiit=None,
word_buffer=None
):
    """
    It is used to get table 
    """
    
    columns= get_view_column(database,view_name)
    table_names=get_view_table(database,view_name)
    lazy_data=asyncio.run(row__multiple_table(database,table_names,columns,limit_row=row_limiit,word_buffer=word_buffer))

    #LAZY_DATA is false when no data in table
    if lazy_data is False:
        return False

    # processed = AddFlagsToColumns(database,view_name, columns)
    return tabulate(lazy_data, headers=columns, showindex=index, tablefmt=style)



def drop_primary_key(database,table_name):
    """
    Remove primary key from the flag file
    """
    if not check_table(database,table_name):
        return False

    priamary_key = primary_key_exists(database,table_name)
    if not priamary_key:
        logerror(database,table_name, "PRIMARY KEY : does not exists")
        return False
    loginfo(table_name, "PRIMARY KEY : droped sucessfully")
    writer(PRIMARY_KEY(database,table_name), '', 'w')
    return True


def assign_primary_key(database,table_name, column):
    """
    Assign primary key in the flag file
    """
    if not check_table(database,table_name):
        return False

    primary_key = get_primary_column(database,table_name)

    if column == primary_key:
        logWarning(
            table_name, f"PRIMARY KEY: {column} is already a primary key")
        return False

    if not check_priamary_column(database,table_name, primary_key):
        logerror(
            table_name, "PRIMARY KEY: cannot make it a primary column due to dublication")
        return False

    if not column_exists(database,table_name, column):
        logerror(database,table_name, f"COLUMN : column {column} not in table")
        return False

    if primary_key is None:
        write_element_in_primary(database,table_name, column)
        loginfo(
            table_name, 
            f"COLUMN : sucessfully assigned {column} as primary key"
            )
        return True
    logerror(database,table_name, "COLUMN : primary key already present")
    return False
