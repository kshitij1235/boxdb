'''
boxdb/auth_boxbd -> v0.9

This file contain code for
1)single row auth, and all row auth

'''

from boxdb.core import word_search_line, read_specific_line
from boxdb.support import get_columns, get_primary_column
from boxdb.logs import logerror
from boxdb.settings import COLUMNS

def chech_rows(database,table_name, column_name, user_input):
    """
    this function help you authenticate the single row data validity
    """
    with open(COLUMNS(database,table_name,column_name), encoding='UTF-8') as file_data:
        return user_input in file_data.read()


def auth_details(database,table_name, user_details):
    """
    Authorize the data from the table
    """
    # TODO improve and simplify the code

    # get all the row and primary_keys and even their postion in list

    primary_key = get_primary_column(database,table_name)
    if primary_key is None:
        logerror(database,table_name,"PRIMARY KEY : need atleast one primary column ")
        return False

    rows = get_columns(database,table_name)
    # key_postion = [rows.index(elements) for elements in primary_key]
    primary_column_position = rows.index(primary_key)

    # verify the postion of the column with the help of primary_keys
    primary_key_element_postion = word_search_line(
        COLUMNS(database,table_name,primary_key), user_details[primary_column_position])

    # check for difference in primary_keys data

    final_list = []
    # tally all the data from user and database
    for index, element in enumerate(rows):
        try:
            final_list.append(read_specific_line(COLUMNS(database,table_name,element), 
            primary_key_element_postion-1).strip()
                              == user_details[index])
        except TypeError:
            return False
    return final_list


def specific_auth(database,table_name,rows,user_details):
    """
    Authorize the data from the table
    """

    # get all the row and primary_keys and even their postion in list

    primary_key = get_primary_column(database,table_name)
    
    if primary_key is None and primary_key not in rows:
        logerror(database,table_name,"PRIMARY KEY : need atleast one primary column ")
        return False

    primary_column_position = rows.index(primary_key)

    primary_key_element_postion = word_search_line(
        COLUMNS(database,table_name,primary_key), user_details[primary_column_position])

    final_list=[]
    
    # tally all the data from user and database
    for index,element in enumerate(rows):
        try:
            final_list.append(read_specific_line(COLUMNS(database,table_name,element), primary_key_element_postion-1).strip()
             == user_details[index])

        except TypeError:
            return False
    return final_list