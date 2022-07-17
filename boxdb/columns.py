'''
boxdb/auth_boxbd -> v0.9

This file contain code for all
the row methods

[ ]delete_row() -> added it deleted columns permenently
[ ]remove_row() -> added it does not delete columns permenently
[ ]create_column() -> added feature to create a uniques column
[ ]create_column() -> added feature to create a column with forbident words
'''

# all the import necessary for basic function on files
# and writing file is a particular way 
# there is also a checkup lib that helps with the basic checkups
# that need to be performed on the table 

from boxdb.support import(
    get_columns,
    get_primary_column,
    max_row_size,
    remove_dublicate_columns,
    reformat_file   
)


from boxdb.settings import FORBIDDEN_WORDS

from boxdb.FileWriteup import(
    write_element_in_primary,
    append_element_in_not_null,
    add_blank_lines_in_columns,
    remove_column_and_file,
    register_column,
    remove_column_without_file,
    write_element_in_unique,
    push_list_elements_in_line
)

from boxdb.checkups import(
    column_exists,
    check_table
)

from boxdb.logs import(
    logerror,
    logWarning,
    loginfo
)


def create_column(table_name,
                  columns,
                  primary_key=False,
                  not_null=False,
                  unique=False,
                  Forbiden_words=None
                  ):
    """creates files under table so that data can be stored"""

    if not check_table(table_name):
        return False

    # TODO add unique column function 

    # get all the column names
    content = get_columns(table_name)
    column_lenght = max_row_size(table_name, content)
    primary = get_primary_column(table_name) if primary_key is True else None
    
    # write to data file and make files if in list
    if not isinstance(columns, list):
        columns = [columns]

    # removing already existing columns
    columns = remove_dublicate_columns(table_name, columns)

    for elements in columns:
        if primary is not None and primary_key is True:
            logerror(table_name,f"PRIMARY KEY : You have a primary key already {primary} ")
            return False
        # fill all the empty void with putting null in the file if there is already colucountermns
        if not add_blank_lines_in_columns(table_name, elements, column_lenght):
            logerror(table_name,'COLUMN : could not create')
            return False

        # checks if file exists
        if column_exists(table_name, elements):
            # update the data file in main file

            # Add primary key if doesnt exists
            if primary is None and primary_key is True:
                write_element_in_primary(table_name, elements)
            
            if unique :
                write_element_in_unique(table_name,elements)        

            # Add to not null
            if not_null:
                append_element_in_not_null(table_name, elements)

            register_column(table_name, elements)
            
        if Forbiden_words is not None:
            push_list_elements_in_line(table_name=table_name,
            filename=FORBIDDEN_WORDS(table_name,elements),
            list_elements=Forbiden_words,
            column=elements)

        else:
            logWarning(table_name,f"COLUMN : {elements} could not be created")

    # remove black spaces from the file
    reformat_file(table_name)


    loginfo(table_name,f"COLUMN : Created {len(columns)} Column sucessfully")
    return True


def delete_column(table_name, column):
    """
    removes files under table so that data can be released
    """
# FIXME optimization needed

    if not check_table(table_name):
        return False

    # write to data file and make files if in list
    if not isinstance(column, list):
        column = [column]

    content = get_columns(table_name)
# list input
    # element extractiion from the list
    for elements in column:
        # writing into file when the file is present into data file
        if content.count(elements) == 1:
            remove_column_and_file(table_name, elements)
            loginfo(table_name,f"COLUMN : '{elements}' Deleted sucessfully")
            return True
        logerror(table_name,f"ERROR : '{elements}' not present in table")
        return False


def remove_column(table_name,
                column
                ):
    """
    It doesnt permently delete the column
    """

    if not check_table(table_name):
        return False
        
    # write to data file and make files if in list
    if not isinstance(column, list):
        column = [column]

    content = get_columns(table_name)
    # list input
    # element extractiion from the list
    for elements in column:
        # writing into file when the file is present into data file
        if content.count(elements) == 1:
            remove_column_without_file(table_name, elements)
            loginfo(table_name,f"COLUMN : '{elements}' Removed sucessfully")
            return True

        logerror(table_name,f"ERROR : '{elements}' not present in table")
        return False