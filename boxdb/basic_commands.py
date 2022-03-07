'''
boxdb/basic_commands -> v0.3

This file contain code for
1)row , column creation and deletion
2)and gettting table

changes made
-> get_table() now we can select rows to show
->add_column() is been tweed so it fills empty spaces by null
->create_rows() is been updated soliving spacing problem in data file
'''

from os import remove
from filemod import writer, delete_specific_line, remove_word, write_specific_line
from tabulate import tabulate
from boxdb.support_litebase import get_content, get_rows


def create_row(table_name, rows):
    """creates files under table so that data can be stored"""

    # get all the row names
    content = get_rows(table_name)

    make_rows = []

    # calculate the number of column in each row
    row_lenght = [
        len(
            get_content(
                f"{table_name}/tables/{row}.txt",
                f"{table_name}/tables/{row}.txt",
            )
        )
        for row in content
    ]

    # write to data file and make files if in list

    if not isinstance(rows, list):
        make_rows.append(rows)
    else:
        make_rows = rows

    for elements in make_rows:
        # this check redundancy in the table and avoid it
        if elements in content:
            print(f"Row {elements} already exists")
            continue
        # fill all the empty void with putting null in the file
        writer(f"./{table_name}/tables/{elements}.txt",
               "null \n"*max(row_lenght), "w")
        # update the data file
        write_specific_line(f"./{table_name}/{table_name}_data.txt", len(content)+1,
                            f"{elements} \n")
    
    with open(f"./{table_name}/{table_name}_data.txt", 'r+',encoding="UTF-8") as fd:
        lines = fd.readlines()
        fd.seek(0)
        fd.writelines(line for line in lines if line.strip())
        fd.truncate()
        
    print(f"Created {len(content)} rows sucessfully")


def remove_row(table_name, row):
    """removes files under table so that data can be released"""

    content = get_content(f"{table_name}_data.txt",
                          f"{table_name}/{table_name}_data.txt")

# list input
    if isinstance(row, list):
        # element extractiion from the list
        for elements in row:
            # writing into file when the file is present into data file
            if content.count(elements) == 1:
                remove_word(f"{table_name}/{table_name}_data.txt", elements)
                remove(f"./{table_name}/tables/{elements}.txt")
            else:
                print(f"ERROR : {elements} not present in table")

# string input
    elif content.count(row) == 1:
        remove_word(f"{table_name}/{table_name}_data.txt", row)
        remove(f"./{table_name}/tables/{row}.txt")

    else:
        print(f'ERROR : {row} not present in table')


def add_column(table_name, data_in_array):
    """removes files under table so that data can be released"""

    content = get_rows(table_name)

    # writing into file and check for the actually number of row and inputs
    if len(content) == len(data_in_array):
        for rows, column in zip(content, data_in_array):
            writer(
                f"./{table_name}/tables/{rows}.txt", f"{column} \n", "a")

    else:
        print("Number of column are either greater or less")


def get_table(table_name, rows=None):
    """
    It is used to display table in terminal or even filture
    out some rows according to the convience
    """

    table = []
    if rows is None:
        rows = []

    # get the number of rows

    content = get_rows(table_name)

    if rows != []:
        content = rows

    # get columns in the row
    for row in content:
        row_content = get_content(
            f"{row}.txt", f"./{table_name}/tables/{row}.txt")
        table.append(row_content)
    higest_col = max(map(len, table))

    # filter the empty or half filled list to replace with null
    for item in table:
        if len(item) < higest_col:
            for _ in range(higest_col):
                if len(item) != higest_col:
                    item.append("null")
    result = [[table[j][i]
               for j in range(len(table))] for i in range(len(table[0]))]

    print(tabulate(result, headers=content, tablefmt="grid"))
    print(f"Table config = {len(get_rows(table_name))}x{higest_col}")
    return True


def remove_column_number(table_name, column_number):
    """
    removing colums with refrence of the number
    """
    content = get_content(
        "row names ", f"./{table_name}/{table_name}_data.txt")
    print(content)
    for rows in content:
        try:
            delete_specific_line(
                f"./{table_name}/tables/{rows}.txt", column_number)
        except Exception:
            print(f"ERROR : column number {column_number} not found")
