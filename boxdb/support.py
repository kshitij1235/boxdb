'''
boxdb/support_litebase -> v0.9

This file contain code for
1)get the data from file, and get row data

AddFlagsToColumns()->fixed major bug

'''

from boxdb.core import(read_specific_line,
get_limited_lines,
number_of_lines,
writer
)

from boxdb.tempo_core import(
    extract_keys,
    extract_values,
    extract_data
)

from boxdb.logs import logerror

from boxdb.settings import (FORBIDDEN_COLUMNS, 
FORBIDDEN_WORDS, 
PRIMARY_KEY,
NOT_NULL,
UNIQUE,
COLUMNS,
COLUMNS_DATA,
VIEW)

def get_content(context, target,limit=None,word_buffer=None):
    """
    It gets the content from any file with
    data in it(auto generated) and returns in list
    """
    #FIXME optimization need takes 0.009 secs

    lines = []
    temp=[]
    counter=0
    try:        
        if limit !=None:
            return get_limited_lines(target,limit)

        with open(target,encoding='UTF-8') as file:
            lines = file.readlines() 
        
        if word_buffer is not None:
            for elemnets in lines :
                temp.append(f"{elemnets[0:word_buffer]}{''if len(elemnets)<=word_buffer else '...'}")
                lines=temp
        del temp
        return list(map(str.strip, lines))

    except FileNotFoundError:
        print(f"{context} {target} file missing")
        return False

#FIXME might need changes after
def get_columns(database,table_name):
    """
    It gets the content from any file with
    data in it(auto generated) and returns in list
    """
    return extract_keys(COLUMNS_DATA(database,table_name))

def get_view(database,view_name):
    """
    It gets content in view
    """
    return extract_data(VIEW(database,view_name))

def get_view_table(database,view_name):
    """
    It gets content in view
    """
    return extract_values(VIEW(database,view_name))

def get_view_column(database,view_name):
    """
    It gets content in view
    """
    return extract_keys(VIEW(database,view_name))

def get_columns_datatype(database,table_name):
    """
    It gets the content from any file with
    data in it(auto generated) and returns in list
    """
    return extract_values(COLUMNS_DATA(database,table_name))

def get_all_columns(database,table_name):
    """
    Get all the types of column in a single dictonary
    """
    all_columns = {'columns': get_columns(database,table_name)}
    all_columns['primary_key']=get_primary_column(database,table_name)
    all_columns['not_null']=get_not_null_columns(database,table_name)
    return all_columns    

def get_primary_column(database,table_name):
    """
    This gets all the primary key columns from the table
    """
    line = read_specific_line(PRIMARY_KEY(database,table_name),0)
    return None if line is False else line



def get_not_null_columns(database,table_name):
    """
    This gets all the not null columns from the table
    """
    return get_content("not null column ",NOT_NULL(database,table_name))

def get_unique_columns(database,table_name):
    """
    This gets all the unique columns from the table
    """
    return get_content("unique column ",UNIQUE(database,table_name))

def get_forbidden_columns(database,table_name):
    """
    This gets all the forbidden columns from the table
    """
    return get_content("forbidden words ",FORBIDDEN_COLUMNS(database,table_name))

def get_forbidden_words(database,table_name,column):
    return get_content("row",FORBIDDEN_WORDS(database,table_name,column))

def get_elements(database,table_name,column):
    """
    get values from column
    """
    with open(COLUMNS(database,table_name,column),'r+',encoding="UTF-8") as files:
        line=files.readlines()
        
    return [row_elements.strip() for row_elements in line]

def reformat_file(database,table_name):
    """
    removes blank line from anyfile 
    """
    with open(COLUMNS_DATA(database,table_name), 'r+', encoding="UTF-8") as file:
        lines = file.readlines()
        file.seek(0)
        file.writelines(line for line in lines if line.strip())
        file.truncate()
    return True

def max_row_size(database,table_name,columns):
    """
    get the maximum row size of table
    """
    if not isinstance(table_name, list):
        table_name= [table_name]
    rows_amount=[]

    if isinstance(table_name,str):
        for column in columns:
            rows_amount.append(number_of_lines(COLUMNS(database,table_name,column)))
        return max(rows_amount)-1 if rows_amount else 0

    for table,column in zip(table_name,columns):
        rows_amount.append(number_of_lines(COLUMNS(database,table,column)))
    return max(rows_amount)-1 if rows_amount else 0



def remove_dublicate_columns(database,table_name,colums):
    """
    remove thee columns that alreay exist in main table
    """
    main_column=get_columns(database,table_name)
    for elements in colums:
        if elements in main_column:
            logerror(database,table_name,f'COLUMN : column {elements} already exists')
            colums.remove(elements)
    return colums

def AddFlagsToColumns(database,table_name,content):
    """
    Add flags in Brackets according to the types of column
    """
    processed=[]

    # get primary key and not null keys 
    primary_keys = get_primary_column(database,table_name)
    not_null=   get_not_null_columns(database,table_name)
    unique=get_unique_columns(database,table_name)
    forbidden=get_forbidden_columns(database,table_name)


    # Assign flag and add to list
    for column in content:
        flags_gpr=column
        if primary_keys is not None and flags_gpr in primary_keys:
            flags_gpr = f"{flags_gpr}(P)"
        elif flags_gpr in not_null:
            flags_gpr = f"{flags_gpr}(N)"
        elif flags_gpr in unique:
            flags_gpr = f"{flags_gpr}(U)"
        elif flags_gpr in forbidden:
            flags_gpr = f"{flags_gpr}(F)"
        processed.append(flags_gpr)
    return processed

def generate_array(data):
    """generate string arrays to real arrays"""
    array_temp = []
    array = []
    for array_elements in data:
        if array_elements in ["["]:
            continue
        elif array_elements in [",", "]"]:
            if isinstance(collab_words_in_list(array_temp), int):
                array.append(int(collab_words_in_list(array_temp)))
            else:
                array.append(collab_words_in_list(array_temp))
            array_temp.clear()
        else:
            array_temp.append(array_elements)
    return array

def collab_words_in_list(list):
    """collab word into strings"""
    return ''.join(list)

def number_string(data):
    """Detect the nature of letter is number or not"""
    try:
        return int(data)
    except Exception:
        return str(data)

def allot_values(values):
    """
    typecasting smartly
    """
    processed_values=[]
    for elements in values:
        if elements[0] == "[":
            processed_values.append(list(generate_array(elements)))
        elif elements=="True":
            processed_values.append(True)
        elif elements=="False":
            processed_values.append(False)
        else:   
            processed_values.append(number_string(elements))
    return processed_values

def convert_list_elements_to_string(input_list):
    """
    convert different elements of list to string in 
    list
    """
    converted_list=[]
    for element in input_list:
        converted_list.append(str(element))
    return converted_list

def write_dict(filename,keys,values):
    writing_file="{ \n"
    for key, value in zip(keys,values):
        writing_file = f"{writing_file}{key}:{value}\n"
    writing_file = writing_file+"\n"+"}"
    writer(filename,writing_file,"w")
    return True

def type_cast_list(List,type_):
    """
    Type cast a list with certain data type
    """
    data=list(map(type_,List))
    return data

