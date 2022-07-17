from boxdb.settings import COLUMNS

from boxdb.support import (get_content,
get_columns)

from boxdb.checkups import (table_struture_exists,
check_table)

async def row_table(table_name, columns):
    table = []
    if not check_table(table_name):
        return False

    if columns is None:
        columns = get_columns(table_name)

    # get the number of columns
    content = get_columns(table_name)

    if not table_struture_exists(table_name):
        return False

    # if no column input assume it to be content
    if columns != []:
        content = columns

    # get the amount of rows in column and calculate the higest
    for column in content:
        row_content = get_content(
            f"{column}.txt", COLUMNS(table_name, column))
        table.append(row_content)
    higest_col = max(map(len, table))

    # filter the empty or half filled list to replace with null
    for item in table:
        if len(item) < higest_col:
            for _ in range(higest_col):
                if len(item) != higest_col:
                    item.append("null")

    return [[table[j][i] for j in range(len(table))] for i in range(len(table[0]))]
