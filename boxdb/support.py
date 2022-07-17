'''
boxdb/support_litebase -> v0.9

This file contain code for
1)get the data from file, and get row data

[ ]MaxRowSize(table_name,columns) -> added
[ ]reformat_file(table_name) -> added

'''

from filemod import read_specific_line
from boxdb.settings import FORBIDDEN_COLUMNS, FORBIDDEN_WORDS, PRIMARY_KEY,NOT_NULL,UNIQUE

def get_content(context, target):
    """
    It gets the content from any file with
    data in it(auto generated) and returns in list
    """
    #FIXME optimization need takes 0.009 secs
    lines = []
    try:        
        with open(target,encoding='UTF-8') as file:
            lines = file.readlines() 
        lines= list(map(str.strip, lines))
    except FileNotFoundError:
        print(f"{context} file missing")
        return False
    return lines

def get_columns(table_name):
    """
    It gets the content from any file with
    data in it(auto generated) and returns in list
    """
    lines = []
    try:
        lines=get_content('COLUMN : ',f"{table_name}/{table_name}_data.txt")
    except FileNotFoundError:
        print("column file missing")
    return lines

def get_all_columns(table_name):
    """
    Get all the types of column in a single dictonary
    """
    all_columns = {'columns': get_columns(table_name)}
    all_columns['primary_key']=get_primary_column(table_name)
    all_columns['not_null']=get_not_null_columns(table_name)
    return all_columns    

def get_primary_column(table_name):
    """
    This gets all the primary key columns from the table
    """
    line = read_specific_line(PRIMARY_KEY(table_name),0)
    if line is False:
        return None
    return line

def get_not_null_columns(table_name):
    """
    This gets all the not null columns from the table
    """
    return get_content("not null column ",NOT_NULL(table_name))

def get_unique_columns(table_name):
    """
    This gets all the unique columns from the table
    """
    return get_content("unique column ",UNIQUE(table_name))

def get_forbidden_columns(table_name):
    """
    This gets all the forbidden columns from the table
    """
    return get_content("forbidden words ",FORBIDDEN_COLUMNS(table_name))

def get_forbidden_words(table_name,column):
    return get_content("row",FORBIDDEN_WORDS(table_name,column))

def get_elements(table_name,column):
    """
    get values from column
    """
    with open(f'.\\{table_name}\\tables\\{column}.txt','r+',encoding="UTF-8") as files:
        line=files.readlines()
    return [elements.strip() for elements in line]

def reformat_file(table_name):
    """
    removes blank line from anyfile 
    """
    with open(f"./{table_name}/{table_name}_data.txt", 'r+', encoding="UTF-8") as file:
        lines = file.readlines()
        file.seek(0)
        file.writelines(line for line in lines if line.strip())
        file.truncate()
    return True

def max_row_size(table_name,columns):
    """
    get the maximum row size of table
    """
    return max([len(get_content(f"{table_name}/tables/{column}.txt",
                         f"{table_name}/tables/{column}.txt",)) for column in columns] if columns else [0])


def remove_dublicate_columns(table_name,colums):
    """
    remove thee columns that alreay exist in main table
    """
    main_column=get_columns(table_name)
    for elements in colums:
        if elements in main_column:
            print(f'COLUMN : column {elements} already exists')
            colums.remove(elements)
    return colums

def AddFlagsToColumns(table_name,content):
    """
    Add flags in Brackets according to the types of column
    """
    processed=[]
    # get primary key and not null keys 
    primary_keys = get_primary_column(table_name)
    not_null= get_not_null_columns(table_name)

    # Assign flag if no primary key and add to list 
    if primary_keys is None:
        for column in content:
            if column in not_null:
                processed.append(f"{column}(N)")
            else:
                processed.append(column)
        return processed

    # Assign flag and add to list 
    for column in content:
        if column in not_null and column in primary_keys:
            processed.append(f"{column}(P)(N)")
        elif column in not_null:
            processed.append(f"{column}(N)")
        elif primary_keys is None:
            continue
        elif column in primary_keys:
            processed.append(f"{column}(P)")
        else:
            processed.append(column)
    return processed

