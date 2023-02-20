from boxdb.support import get_elements
from boxdb.settings import COLUMNS_DATA, COLUMNS
from boxdb.tempo_core import extract_data
from boxdb.support import type_cast_list,get_columns
import asyncio

def column_data(database,table_name,column,typecasting=True):
    """
    Return column of elements in its true data form
    """

    # get data type of column 
    column_datatype=extract_data(COLUMNS_DATA(database,table_name))[column]
    
    # get data of column 
    column_elements =get_elements(database,table_name,column) 
     
    if typecasting:
        # Type cast elements  
        if column_datatype == "int":
            return type_cast_list(column_elements,int)
        if column_datatype == "bool":
            return type_cast_list(column_elements,bool)
    return column_elements


def table_data(database,table_name,columns=None,row_limit=None,word_buffer=None):
    """
    returns you the table data in list
    """
    from boxdb.readtable import row_table
    if columns is None :
        columns=get_columns(database,table_name)

    lazy_data=asyncio.run(row_table(database,table_name,columns,limit_row=row_limit,word_buffer=word_buffer))
    return lazy_data
