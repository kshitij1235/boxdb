from boxdb.settings import COLUMNS

from boxdb.support import (get_content,
get_columns,
max_row_size)

from boxdb.checkups import (table_struture_exists,
check_table)

from boxdb.Table_data import column_data

"""
[ ] row_table() -> Made improvements
"""

async def row_table(database,table_name, columns,limit_row=None,word_buffer=None):
 
    table = []
    higest_col=0

    if not check_table(database,table_name):
        return False

    if not table_struture_exists(database,table_name):
        return False

    higest_col = max_row_size(database,table_name,columns)

    # get the amount of rows in column and calculate the higest
    for column in columns:
        column_content = column_data(database,table_name,column)
        table.append(column_content)

    # filter the empty or half filled list to replace with null
    for column_elements in table:
        if len(column_elements) < higest_col:
            for _ in range(higest_col):
                if len(column_elements) != higest_col:
                    column_elements.append("null")

    return [[table[j][i] for j in range(len(table))] for i in range(len(table[0]))]



async def row__multiple_table(database,table_names, columns,limit_row=None,word_buffer=None):

    table = []
    for table_name , column in zip(table_names,columns):
        if not check_table(database,table_name):
            return False

        if not table_struture_exists(database,table_name):
            return False

        max_row = max_row_size(database,table_names,columns)

        # get the amount of rows in column and calculate the higest
        row_content = get_content(
            f"{column}.txt", COLUMNS(database,table_name, column),limit=limit_row,word_buffer=word_buffer)
        table.append(row_content)

        # filter the empty or half filled list to replace with null
        for item in table:
            if len(item) < max_row:
                for _ in range(max_row):
                    if len(item) != max_row:
                        item.append("null")
    print(item)
    return [[table[j][i] for j in range(len(table))] for i in range(len(table[0]))]
