from boxdb.settings import COLUMNS

from boxdb.support import (get_content,
get_columns,
max_row_size)

from boxdb.checkups import (table_struture_exists,
check_table)

async def row_table(database,table_name, columns,limit_row=None):
 
    table = []
    higest_col=0
    if not check_table(database,table_name):
        return False

    if columns is None:
        columns = get_columns(database,table_name)

    # get the number of columns
    content = get_columns(database,table_name)

    if not table_struture_exists(database,table_name):
        return False

    # if no column input assume it to be content
    if columns != []:
        content = columns

    max_row = max_row_size(database,table_name,columns)
    if limit_row is not None and max_row < limit_row :
        limit_row=max_row
        higest_col = limit_row
    elif limit_row is None:
        higest_col = max_row


    # get the amount of rows in column and calculate the higest
    for column in content:
        row_content = get_content(
            f"{column}.txt", COLUMNS(database,table_name, column),limit=limit_row)
        table.append(row_content)
    # filter the empty or half filled list to replace with null
    for item in table:
        if len(item) < higest_col:
            for _ in range(higest_col):
                if len(item) != higest_col:
                    item.append("null")

    return [[table[j][i] for j in range(len(table))] for i in range(len(table[0]))]
