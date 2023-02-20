'''
boxdb/tempo_core.py - version 1.4.6

[ ]extract_keys()-> fixed bugs
'''


from boxdb.core import writer, reader



def extract_keys(filename):
    """
    extract keys from file
    1)this takes list or some times even file works. 
    2)finds for each specific line where '\n' is present(this means new line)
    3)and append every thing before ':' and append it in a list
    """
    from boxdb.support import  allot_values,collab_words_in_list
    txt_file_data=list(reader(filename))
    temp = []
    keys = []
    for index , element in enumerate(txt_file_data) :
        if element== "\n":
            for value_index in range(index, len(txt_file_data)):
                if txt_file_data[value_index] == ":":
                    keys.append(collab_words_in_list(temp))
                    temp.clear()
                    break
                elif txt_file_data[value_index] not in [":","}", "{"]:
                    temp.append(txt_file_data[value_index])

    keys=list(map(str.strip, keys)) 
    res = []
    [res.append(x) for x in keys if x not in res]          
    return res


def extract_values(filename):
    """extract values from file"""
    from boxdb.support import  allot_values,collab_words_in_list
    temp = []
    values = []
    txt_file_data=list(reader(filename))
    for index ,element in enumerate(txt_file_data):
        if element == ":":
            for index in range(index, len(txt_file_data)):
                if txt_file_data[index] == "\n":
                    values.append(collab_words_in_list(temp))
                    temp.clear()
                    break
                elif txt_file_data[index] not in [":", "'", " ", '"', "}", '\r']:
                    temp.append(txt_file_data[index])
    values = allot_values(values)
    return values

def extract_data(data):
    """create a dictonary"""

    keys = extract_keys(data)
    values = extract_values(data)
    res = []
    [res.append(x) for x in keys if x not in res]
    keys=res
    return {keys[index]: values[index] for index in range(len(keys))}

def edit_data(filename, key, value):
    """
    edit value  from the file
    """
    
    data = list(reader(filename))
    keys = extract_keys(data)
    values = extract_values(data)

    # gettting value of element to change

    temp = keys.index(key)

    # swaping the old value witgh new one 

    values.pop(temp)
    values.insert(temp, value)

    # filling template   

    writing_file = '{ \n'
    for key , value in zip(keys,values):
        writing_file = f"{writing_file}{key}:{value}\n"
    writing_file = writing_file+"\n"+"}"
    
    # writing the date processed 
    writer(filename, writing_file, "w")
    return True


def add_data(filename, newkeys, newvalues):
    """append data into txt file"""
    # get the file data

    # extract keys and values
    keys = extract_keys(filename)
    values = extract_values(filename)

    # append new keys and values to old list
    keys.append(newkeys)
    values.append(newvalues)

    # filling up template

    write_file = "{ \n"

    for size in range(len(keys)):
        write_file = f"{write_file} {keys[size]} : {values[size]}\n"

    write_file = write_file+"\n"+"}"

    # write in file
    writer(filename, write_file, "w")

    return True

def remove_value(filename,key):

    keys=extract_keys(filename)
    values=extract_values(filename)

    index=keys.index(key)

    keys.remove(key)
    values.pop(index)
    writing_file="{ \n"
    for keys , values in zip(keys,values):
        writing_file = f"{writing_file}{keys}:{values}\n"
    writing_file = writing_file+"\n"+"}"
    writer(filename,writing_file,"w")