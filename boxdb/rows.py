from filemod import delete_specific_line
from boxdb.settings import COLUMNS


from boxdb.support import (
    get_forbidden_columns,
    get_primary_column,
    get_not_null_columns,
    get_unique_columns,
    get_columns
)

from boxdb.FileWriteup import(
    replace_column_element_with_pk_refrence,
    word_search_line,
    replace_column_element_with_pk_refrence,
    write_rows_and_columns_in_file,
    delete_a_specific_row
)

from boxdb.checkups import(
    row_element_exist,
    primary_key_exists,
    empty_table,
    check_table
)

from boxdb.logs import(
    logerror,
    loginfo,
)

def add_row(table_name, data_in_array):
    """removes files under table so that data can be released"""

    # TODO addrow() function is way too complicated
    # TODO notnull is broken

    if not check_table(table_name):
        return False

    content = get_columns(table_name)

    # get all the primary column to detect dublication
    primary_key = get_primary_column(table_name)
    not_null_key = get_not_null_columns(table_name)
    unique_key = get_unique_columns(table_name)
    forbidden_key=get_forbidden_columns(table_name)

    # writing into file and check for the actually number of row and inputs
    if len(content) != len(data_in_array):
        logerror(table_name,"ROW: Imblance number of rows")
        return False

    for column, rows in zip(content, data_in_array):
        
        # this checks for the double entry in table of primary column
        if primary_key is not None and column in primary_key and row_element_exist(table_name, column, rows):
            # if dublication is found
            logerror(table_name,f"PRIMARY KEY : {rows} exits in the {column}")
            return False
        if unique_key  is not None and column in unique_key and row_element_exist(table_name, column, rows):
            # if dublication is found
            logerror(table_name,f"UNIQUE : {rows} exits in the {column}")
            return False
        if not_null_key is not None and column in not_null_key and rows in ['null', " "]:
            logerror(table_name,f"NOT NULL : {column} cannot be empty or null")
            return False

    # # puting rows into columns
    if write_rows_and_columns_in_file(table_name,content,data_in_array,forbidden_key):
        return True


def remove_row_number(table_name, row_number):
    """
    removing colums with refrence of the number
    """
    if not check_table(table_name):
        return False

    content = get_columns(table_name)
    for column in content:
        try:
            delete_specific_line(
                f"./{table_name}/tables/{column}.txt", row_number)
        except FileNotFoundError:
            logerror(table_name,f"ROW : ROW number {row_number} not found")
            return False

    loginfo(table_name,f"ROW : ROW number {row_number} sucessfully cleared")
    return True

def remove_row(table_name,primary_key, row_element):
    """
    This removes rows for the specific table
    which is accqqured by the table_name 

    primary key-> is the primary column refrence
    which is very important with that it wont delete a row
    
    row elements is the acutally a element from primary column
    for the refrece of row to remove

    """

    if not check_table(table_name):
        return False

    # check if table is empty or not
    if not empty_table(table_name):
        return False

    # check for primary key exists
    primary = primary_key_exists(table_name)
    if not primary:
        return False

    # check if refrence is give =n correctly
    if primary_key not in primary:
        logerror(table_name,"ROW : refrence not in primary column")
        return False

    rows = get_columns(table_name)

    # serarching for a the line to remove
    row_to_remove = word_search_line(
        COLUMNS(table_name,primary_key), row_element)
    
    if row_to_remove is False:
        logerror(table_name,f"ROW : element {row_element} not found in {primary_key}")
        return False

    # deleting row from all the files
    return delete_a_specific_row(table_name,rows,row_to_remove,row_element)



def update_row(table_name,
               primary_value,
               column,
               replace,
               element_to_change=None):
    """
    This changes the values from the table
    primary_vale -> its a refrence value to get the row number
    column -> its to get which row to change
    replace -> it is what row element will be updated in

    element_to_change is kept None -> then the table will automatically 
    search for the element , but its a little slow

    if element_to_change is given it will work a lot faster
    but at the same time you have to specify the element that you
    want to replace

    """

    # performing checks 

    if not check_table(table_name):
        return False

    primary_column = get_primary_column(table_name)

    # check primary key
    if primary_column is None:
        logerror(table_name,"PRIMARY KEY : not found")
        return False

   # search for primary key with element
    return replace_column_element_with_pk_refrence(table_name,
        primary_column,
        primary_value,
        column, replace,
        element_to_change)
