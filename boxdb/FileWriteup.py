from os import remove
from boxdb.checkups import column_exists
from boxdb.tempo_core import(
    add_data,
    edit_data,
    remove_value
)
from boxdb.core import(
    delete_specific_line,
    word_search_line,
    writer,
    write_specific_line,
    read_specific_line
)

from boxdb.settings import(
    COLUMNS_DATA,
    FORBIDDEN_COLUMNS,
    FORBIDDEN_WORDS,
    PRIMARY_KEY,
    NOT_NULL,
    COLUMNS,
    UNIQUE
)

from boxdb.logs import(
    logerror,
    loginfo
)
from boxdb.support import get_forbidden_words

def remove_column_and_file(database,table_name, element):
    """
    Remove column from data file
    Remove column file
    """
    path = COLUMNS_DATA(database,table_name)

    remove_value(path,element)
    return True

def remove_column_without_file(database,table_name, element):
    """
    Remove column from data file
    """
    path = COLUMNS_DATA(database,table_name)
    remove_value(path,element)

    return True


def register_column(database,table_name, column_name,data_type):
    """
    Add column name to file
    """
    add_data(COLUMNS_DATA(database,table_name),column_name,data_type)


def write_element_in_primary(database,table_name, element):
    """
    Push element to the primary flag
    """
    writer(PRIMARY_KEY(database,table_name), f"{element}", "w")

def write_element_in_unique(database,table_name, element):
    """
    Push element to the unique flag
    """
    writer(UNIQUE(database,table_name), f"{element}", "w")

def write_element_in_forbidden(database,table_name, element):
    """
    Push element to the unique flag
    """
    writer(FORBIDDEN_COLUMNS(database,table_name), f"{element}", "w")

def create_forbiddent_file(database,table_name,column):
    writer(FORBIDDEN_WORDS(database,table_name,column),"","w")

def append_element_in_not_null(database,table_name, element):
    """
    Push element to the not null flag
    """
    writer(NOT_NULL(database,table_name), f"{element}\n", "a")


def add_blank_lines_in_columns(database,table_name, column, times):
    """
    fill up the column with dummy lines
    """

    # this helps to retrive file when deleted from column list but 
    # not actual column file is deleted
    if column_exists(database,table_name,column):
        return True
    return writer(COLUMNS(database,table_name,column),
                  " \n"*times, "w")


def replace_column_element_with_pk_refrence(database,
                                            table_name,
                                            primary_columns,
                                            primary__refrence_element,
                                            column_name,
                                            replacement,
                                            target_element=None
                                            ):
    """
    Replace primary_refrence_element to element

    column_name is the targeted column where a change is the made

    were primary_column is a primary column 
    and primary_refrence_element is the refrence element to get the row number

    now we have primary column and the row number will search for the the element in 
    column_name

    if target_element no computation is needed to search from the element but itas optional

    and then will change the element from the replacement
    """

    # get the line number from the changing column
    line = word_search_line(
        COLUMNS(database,table_name,primary_columns), primary__refrence_element)

    if target_element is None:
        # get the name of element to change
        target_element = read_specific_line(
            COLUMNS(database,table_name,column_name), line-1).strip()

    # exit point check if the replacement or changing element is same
    if target_element == replacement:
        logerror(database,table_name,f"TABLE : Column {column_name} is already {target_element}")
        return False

    # change the element
    write_specific_line(
        COLUMNS(database,table_name,column_name), line, replacement)
    loginfo(table_name,
        f"TABLE : changes made in {column_name},from {target_element} -> {replacement}")
    return True



def write_rows_and_columns_in_file(database,table_name,
                                columns,
                                rows,
                                forbidden_keys):
    """
    fills out colums according to the row inputs 
    """

    if forbidden_keys is not None:
        for column , row in zip(columns,rows):
            if column in forbidden_keys:
                resticted_words=get_forbidden_words(database,table_name,column)
                if row in resticted_words:
                    logerror(database,table_name,f"FORBIDDEN : word found {row}")
                    return False

    
    for column, row in zip(columns, rows):
        # adding rows into columns
        writer(COLUMNS(database,table_name,column), f"{row} \n", "a")
    loginfo(database,table_name, f"ROW : sucessfully added to '{table_name}'")
    return True


def delete_a_specific_row(database,table_name,
        rows,
        row_to_remove,
        row_element
        ):
    """
    this delete rows specified in -> row_to_remove
    row_element is specific row element to remove 

    """
    for elements in rows:
        try:
            delete_specific_line(
                COLUMNS(database,table_name,elements), row_to_remove)
        except Exception:
            logerror(database,table_name, f"ROWS : '{row_element}' not found ")
            return False
    loginfo(database,table_name, f"ROWS : '{row_element}' deleted sucessfully")
    return True

def remove_element_with_linenumber(database,table_name,column,line):
    """
    removes a specific row element from a specfic
    column by specifing the line number
    """
    return delete_specific_line(COLUMNS(database,table_name,column), line)

def push_list_elements_in_line(database,table_name,filename,list_elements,column):
    """
    place elements line by line in a file
    """
    for elements in list_elements:
        writer(filename,f"{elements}\n","a")
    write_element_in_forbidden(database,table_name,column)
    return True