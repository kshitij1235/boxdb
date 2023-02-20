'''
boxdb/auth_boxbd -> v0.9

This file contain code for all
the row methods

[ ] rename_column() -> function added

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

from boxdb.settings import FORBIDDEN_WORDS,COLUMNS_DATA,COLUMNS,DATABASE_TABLE

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

from boxdb.tempo_core import edit_keys,edit_data

from os import rename

def create_column(database,
                  table_name,
                  columns,
                  data_type=None,
                  primary_key=False,
                  not_null=False,
                  unique=False,
                  Forbiden_words=None
                  ):
    """creates files under table so that data can be stored"""

    supported_data_types=["int","str","bool"]

    if data_type not in supported_data_types:
        logerror(database,table_name,"COLUMN: Unsupported datatype")
        return False
    
    if not check_table(database,table_name):
        return False

    # TODO add unique column function 

    # get all the column names
    content = get_columns(database,table_name)
    column_lenght = max_row_size(database,table_name, content)
    primary = get_primary_column(database,table_name) if primary_key is True else None
    
    # write to data file and make files if in list
    if not isinstance(columns, list):
        columns = [columns]

    # removing already existing columns
    columns = remove_dublicate_columns(database,table_name, columns)
    if columns==[]:
        return False
    for elements in columns:
        if primary is not None and primary_key is True:
            logerror(database,table_name,f"PRIMARY KEY : You have a primary key already {primary} ")
            return False
        # fill all the empty void with putting null in the file if there is already colucountermns
        if not add_blank_lines_in_columns(database,table_name, elements, column_lenght):
            logerror(database,table_name,'COLUMN : could not create')
            return False

        # checks if file exists
        if column_exists(database,table_name, elements):
            # update the data file in main file

            # Add primary key if doesnt exists
            if primary is None and primary_key is True:
                write_element_in_primary(database,table_name, elements)
            
            if unique :
                write_element_in_unique(database,table_name,elements)        

            # Add to not null
            if not_null:
                append_element_in_not_null(database,table_name, elements)

            register_column(database,table_name, elements,data_type)
        else:
            logWarning(database,table_name,f"COLUMN : {elements} could not be created")
            
        if Forbiden_words is not None:
            push_list_elements_in_line(database,table_name=table_name,
            filename=FORBIDDEN_WORDS(database,table_name,elements),
            list_elements=Forbiden_words,
            column=elements)

    # remove black spaces from the file
    reformat_file(database,table_name)
    edit_data(DATABASE_TABLE(database),table_name,str(len(content)+1))
    loginfo(database,table_name,f"COLUMN : Created {len(columns)} Column sucessfully")
    return True


def delete_column(database,table_name, column):
    """
    removes files under table so that data can be released
    """
    # FIXME optimization needed

    if not check_table(database,table_name):
        return False

    # write to data file and make files if in list
    if not isinstance(column, list):
        column = [column]

    content = get_columns(database,table_name)

    # element extractiion from the columns that need to be deleted
    for element in column:
        # if column that need to be deleted actually exists in the main columns
        if element in content:
            remove_column_and_file(database,table_name, element)
            loginfo(database,table_name,f"COLUMN : '{element}' Deleted sucessfully")
        else:
            logerror(database,table_name,f"ERROR : '{element}' not present in table")
            return False
    edit_data(DATABASE_TABLE(database),table_name,str(len(content)-1))
    return True


def remove_column(database,table_name,column):
    """
    It doesnt permently delete the column
    """

    if not check_table(database,table_name):
        return False
        
    # write to data file and make files if in list
    if not isinstance(column, list):
        column = [column]

    content = get_columns(database,table_name)
    # list input
    # element extractiion from the list
    for elements in column:
        # writing into file when the file is present into data file
        if content.count(elements) == 1:
            remove_column_without_file(database,table_name, elements)
            loginfo(database,table_name,f"COLUMN : '{elements}' Removed sucessfully")
            edit_data(DATABASE_TABLE(database),table_name,str(len(content)-1))  
            return True

        logerror(database,table_name,f"ERROR : '{elements}' not present in table")
        
        return False

def rename_column(database,table_name,column_name,new_column_name):
    '''
    Rename column of the table
    '''
    if column_name not in get_columns(database,table_name):
        logerror(database,table_name,f"COLUMN : column {column_name} does not exits in table {table_name} under {database}")
    edit_keys(COLUMNS_DATA(database,table_name),column_name,new_column_name) 
    rename(COLUMNS(database,table_name,column_name),COLUMNS(database,table_name,new_column_name))
   
    return True
