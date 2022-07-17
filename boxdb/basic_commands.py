'''
boxdb/basic_commands -> v0.9

This file contain code for
1)row,column creation and deletion
2)and gettting table

[ ] add_row() made more faster
[ ] drop_primary_key()->added
[ ] assign_primary_key()->added
[ ] get_table()->loads the table lazyly now and memory effiecient and faster
'''

import asyncio
from filemod import writer
from tabulate import tabulate
from boxdb.settings import PRIMARY_KEY
from boxdb.readtable import row_table
from boxdb.support import (get_primary_column,
get_columns,AddFlagsToColumns )

from boxdb.checkups import (column_exists,
primary_key_exists,
check_priamary_column,
check_table)

from boxdb.FileWriteup import write_element_in_primary
from boxdb.logs import logWarning, loginfo, logerror



def get_table(table_name,
columns=None,
index='always',
style="texttile"
):
    """
    It is used to display table in terminal or even filture
    out some rows according to the convience
    """
    if columns is None:
        columns= get_columns(table_name)
    holy=asyncio.run(row_table(table_name,columns))
    processed = AddFlagsToColumns(table_name, columns)
    return tabulate(holy, headers=processed, showindex=index, tablefmt=style)


def drop_primary_key(table_name):
    """
    Remove primary key from the flag file
    """
    if not check_table(table_name):
        return False

    priamary_key = primary_key_exists(table_name)
    if not priamary_key:
        logerror(table_name, "PRIMARY KEY : does not exists")
        return False
    loginfo(table_name, "PRIMARY KEY : droped sucessfully")
    writer(PRIMARY_KEY(table_name), '', 'w')
    return True


def assign_primary_key(table_name, column):
    """
    Assign primary key in the flag file
    """
    if not check_table(table_name):
        return False

    primary_key = get_primary_column(table_name)
    if column == primary_key:
        logWarning(
            table_name, f"PRIMARY KEY: {column} is already a primary key")
        return False

    if not check_priamary_column(table_name, primary_key):
        logerror(
            table_name, "PRIMARY KEY: cannot make it a primary column due to dublication")
        return False

    if not column_exists(table_name, column):
        logerror(table_name, f"COLUMN : column {column} not in table")
        return False

    if primary_key is None:
        loginfo(
            table_name, f"COLUMN : sucessfully assigned {column} as primary key")
        write_element_in_primary(table_name, column)
        return True
    logerror(table_name, "COLUMN : primary key already present")
    return False
