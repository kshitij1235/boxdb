from filemod import writer, delete_specific_line, remove_word
from boxdb.support_litebase import check_list, get_content, get_rows
from os import remove
from tabulate import tabulate


def create_row(table_name, rows):
    """creates files under table so that data can be stored"""
    # write to data file and make files if in list
    if check_list(rows) == True:
        for elements in rows:
            writer(f"./{table_name}/tables/{elements}.txt", "", "w")
            writer(f"./{table_name}/{table_name}_data.txt",
                   f"{elements} \n", "a")
        print(f"created {len(rows)} rows sucessfully")

    # if in string
    else:
        writer(f"./{table_name}/tables/{rows}.txt", "", "w")
        writer(f"./{table_name}/{table_name}_data.txt", f"{rows} \n", "a")
        print('created 1 rows sucessfully')


def remove_row(table_name, row):
    """removes files under table so that data can be released"""

    content = get_content(f"{table_name}_data.txt",
                          f"{table_name}/{table_name}_data.txt")

# list input
    if check_list(row) == True:
        # element extractiion from the list
        for elements in row:
            # writing into file when the file is present into data file
            if content.count(elements) == 1:
                remove_word(f"{table_name}/{table_name}_data.txt", elements)
                remove(f"./{table_name}/tables/{elements}.txt")
            else:
                print(f"{elements} not present in table")

# string input
    elif content.count(row) == 1:
        remove_word(f"{table_name}/{table_name}_data.txt", row)
        remove(f"./{table_name}/tables/{row}.txt")

    else:
        print(f"{row} not present in table")


def add_column(table_name, data_in_array):
    """removes files under table so that data can be released"""
    content = get_rows(table_name)

    # writing into file and check for the actually number of row and inputs
    if len(content) == len(data_in_array):
        for rows in range(len(content)):
            writer(
                f"./{table_name}/tables/{content[rows]}.txt", f"{data_in_array[rows]} \n", "a")

    else:
        print("Number of column are either greater or less")


def get_table(table_name):

    # get the number of rows
    content = get_content(f"{table_name}_data.txt",
                          f"{table_name}/{table_name}_data.txt")
    table = []

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


def remove_column_number(table_name, column_number):
    content = get_content(
        "row names ", f"./{table_name}/{table_name}_data.txt")
    for rows in content:
        try:
            delete_specific_line(
                f"./{table_name}/tables/{rows}.txt", column_number)
        except:
            pass
