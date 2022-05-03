'''
boxdb/auth_boxbd -> v0.4

This file contain code for
1)single row auth, and all row auth

[ ]auth_details() improved speed
'''
from filemod import word_search_line, read_specific_line
from boxdb.support_litebase import get_columns, get_primary_column


def chech_rows(table_name, rowname, user_input):
    """
    this function help you authenticate the single row data validity
    """
    with open(f'./{table_name}/tables/{rowname}.txt', encoding='UTF-8') as file_data:
        return user_input in file_data.read()

def auth_details(table_name, user_details):
    """
    Authorize the data from the table
    """
    # TODO improve and simplify the code

    # get all the row and primary_keys and even their postion in list

    primary_keys = get_primary_column(table_name)
    if primary_keys == []:
        print("PRIMARY KEY : need atleast one primary row")
        return False

    rows = get_columns(table_name)

    key_postion = [rows.index(elements) for elements in primary_keys]
    # verify the postion of the column with the help of primary_keys
    similarty_data = [
        word_search_line(
            f"./{table_name}/tables/{rows[p_rows]}.txt", user_details[p_rows])
        for p_rows in key_postion
    ]
    # check for difference in primary_keys data
    if similarty_data.count(similarty_data[0]) == len(similarty_data):
        final_list=[]
        # tally all the data from user and database
        for index,element in enumerate(rows):
            try:
                final_list.append(read_specific_line(f"{table_name}/tables/{element}.txt", similarty_data[0]-1).strip()
                 == user_details[index])
            except TypeError:
                return False
    else:
        return False
    return len(user_details) == final_list.count(True)


def specific_auth(table_name,rows,user_details):
    """
    Authorize the data from the table
    """
    # TODO improve and simplify the code

    # get all the row and primary_keys and even their postion in list

    primary_keys = get_primary_column(table_name)
    for extra in [value for value in primary_keys if value not in rows]:
        primary_keys.remove(extra)
    
    if primary_keys == []:
        print("PRIMARY KEY : need atleast one primary row")
        return False

    key_postion = [rows.index(elements) for elements in primary_keys]
    # verify the postion of the column with the help of primary_keys
    similarty_data = [
        word_search_line(
            f"./{table_name}/tables/{rows[p_rows]}.txt", user_details[p_rows])
        for p_rows in key_postion
    ]
    # check for difference in primary_keys data
    if similarty_data.count(similarty_data[0]) == len(similarty_data):
        final_list=[]
        # tally all the data from user and database
        for index,element in enumerate(rows):
            try:
                final_list.append(read_specific_line(f"{table_name}/tables/{element}.txt", similarty_data[0]-1).strip()
                 == user_details[index])
            except TypeError:
                return False
    else:
        return False
    
    if len(user_details)==len(final_list):
        return True