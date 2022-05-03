'''
boxdb/basic_commands -> v0.4

This file contain code for
1)row,column creation and deletion
2)and gettting table

[ ]get_table() doesnt crash if there is not table made
[ ]get_table() added tags for primary key
[ ]create_columns() works better now
[ ]update_rows() added to update row values
[ ]remove_rows() added which work flawless with primary_key refrence    
[ ]remove_columns() made improvements to it 
'''

from os import remove
from os.path import exists
from filemod import writer, delete_specific_line, remove_word, word_find, word_search_line, write_specific_line
from tabulate import tabulate
from boxdb.support_litebase import get_content, get_primary_column, get_columns
from boxdb.table_checkup import check_table


def create_column(table_name, rows, primary_key=False):
    """creates files under table so that data can be stored"""

    # get all the column names
    content = get_columns(table_name)
    column_lenght = [len(get_content(f"{table_name}/tables/{columns}.txt",
                         f"{table_name}/tables/{columns}.txt",)) for columns in content] if content else [0]

    make_columns = []
    # write to data file and make files if in list

    if not isinstance(rows, list):
        make_columns.append(rows)
    else:
        make_columns = rows

    for elements in make_columns:
        # this check redundancy in the table and avoid it
        if elements in content:
            print(f"COLUMN :  {elements} already exists")
            if len(rows) == 1:
                return False
            continue
        # fill all the empty void with putting null in the file if there is already columns
        try:
            writer(f"./{table_name}/tables/{elements}.txt",
                   "null \n"*max(column_lenght), "w")
        except FileNotFoundError:
            print('COLUMN : could not create')

        # checks if file exists
        if exists(f"./{table_name}/tables/{elements}.txt"):
            # update the data file
            writer(f"./{table_name}/{table_name}_data.txt",
                   f"{elements} {'-P'if primary_key else ''} \n", "a")
        else:
            print(f"COLUMN : {elements} could not be created")

   #FIXME try cutting read and write time

    with open(f"./{table_name}/{table_name}_data.txt", 'r+', encoding="UTF-8") as file:
        lines = file.readlines()
        file.seek(0)
        file.writelines(line for line in lines if line.strip())
        file.truncate()

    print(f"COLUMN : Created {len(content)} Column sucessfully")
    return True


def remove_column(table_name, column):
    """removes files under table so that data can be released"""

#FIXME optimization needed
    
    remove_columns=[]
    # write to data file and make files if in list
    if not isinstance(column, list):
        remove_columns.append(column)
    else:
        remove_columns = column

    content = get_columns(table_name)
    path=f"{table_name}/{table_name}_data.txt"
# list input
    # element extractiion from the list
    for elements in remove_columns:
        # writing into file when the file is present into data file
        if content.count(elements) == 1:
            delete_specific_line(path,word_search_line(path,elements))
            remove(f"./{table_name}/tables/{elements}.txt")
        else:
            print(f"ERROR : {elements} not present in table")



def add_row(table_name, data_in_array):
    """removes files under table so that data can be released"""

    #TODO addrow() function is way too complicated

    content = get_columns(table_name)

    # get all the primary column to detect dublication
    primary_key = get_primary_column(table_name)

    # writing into file and check for the actually number of row and inputs
    if len(content) == len(data_in_array):
        catch_rows = []
        catch_col = []

        for column, rows in zip(content, data_in_array):

            # this checks for the double entry in table of primary column
            if column in primary_key:
                # if dublication is found
                print(f"./{table_name}/tables/{column}.txt",rows)
                if word_find(f"./{table_name}/tables/{column}.txt", rows):
                    print(f"PRIMARY KEY : {rows} exits in the {column}")
                    continue
            # if its not forund then stored in classs
                else:
                    catch_rows.append(rows)
                    catch_col.append(column)

        # this is for non primary column
            else:
                catch_rows.append(rows)
                catch_col.append(column)

        # this tally all the catch row and actualy column
        if len(content) == len(catch_col):
            for c_col, c_row in zip(catch_rows, catch_col):
                writer(
                    f"./{table_name}/tables/{c_row}.txt", f"{c_col} \n", "a")
        else:
            print("ERROR")
    else:
        print("Imblance number of rows")


def get_table(table_name, columns=None):
    """
    It is used to display table in terminal or even filture
    out some rows according to the convience
    """

    table = []

    if columns is None:
        columns = []

    # get the number of columns
    content = get_columns(table_name)

    # get primary key 
    primary_keys=get_primary_column(table_name)

    if len(content) <= 0:
        print(f"TABLE : {table_name} has no structure yet")
        return False

    # if no column input assume it to be content
    if columns != []:
        content = columns

    # get the amount of rows in column and calculate the higest
    for column in content:
        row_content = get_content(
            f"{column}.txt", f"./{table_name}/tables/{column}.txt")
        table.append(row_content)
    higest_col = max(map(len, table))

    # filter the empty or half filled list to replace with null
    for item in table:
        if len(item) < higest_col:
            for _ in range(higest_col):
                if len(item) != higest_col:
                    item.append("null")

    # gets all the indivisual rows 

    result = [[table[j][i]
               for j in range(len(table))] for i in range(len(table[0]))]


    # column tag to represent primary_keys
    processed=[]
    for column in content:
        if column in primary_keys:
            processed.append(f"{column}(P)")
        else:
            processed.append(column)

    print(tabulate(result, headers=processed, showindex='always',tablefmt="fancy_grid"),
          f"\nTable config = {len(get_columns(table_name))}x{higest_col}")
    return True


def remove_row_number(table_name, row_number):
    """
    removing colums with refrence of the number
    """
    content = get_columns(table_name)
    for column in content:
        try:
            delete_specific_line(
                f"./{table_name}/tables/{column}.txt", row_number)
        except FileNotFoundError:
            print(f"ERROR : ROW number {row_number} not found")


def remove_row(table_name, column, row_element):
    """
    This removes rows for the table
    """
    rows = get_columns(table_name)
    primary = get_primary_column(table_name)
    if primary ==[]:
        print("PRIMARY KEY : doesnt exist")
        return False
    if column not in primary:
        return False
    row_to_remove = word_search_line(
        f'.\\{table_name}\\tables\\{column}.txt', row_element)
    for elements in rows:
        delete_specific_line(
            f'.\\{table_name}\\tables\\{elements}.txt', row_to_remove)
    return True


def update_row(table_name,primary_value, column, element):
    """
    This changes the values from the table
    """
    # check the existance of table
    if not check_table(table_name):
        print(f"TABLE : {table_name} not found")
        return False

    # check primary key
    primary_rows=get_primary_column(table_name)
    if primary_rows is []:
        print("PRIMARY KEY : not found")
        return False
   
    #search for primary key with element
    for primary_element in primary_rows:    
        if word_find(f'.\\{table_name}\\tables\\{primary_element}.txt', primary_value):
            line=word_search_line(f'.\\{table_name}\\tables\\{primary_element}.txt', primary_value)
            write_specific_line(f'.\\{table_name}\\tables\\{column}.txt',line, element)
            print(f"TABLE : changes made in {primary_element},from row {primary_value}-> {element}")
            return True
        print(f"TABLE : cannot find a primary column {primary_element}")
    return False