def keyword(data,column_number,allow_keyword):
    '''
    give the  data only if it has a matching keyword
    '''
    new_table=[]

    for i in range(len(data)):
        if data[i][column_number] == allow_keyword:
                new_table.append(data[i])

    return new_table

def dontkeyword(data,column_number,restrict_keyword):
    '''
    remove keyord mentioned
    '''
    new_table=[]

    for i in range(len(data)):
        if data[i][column_number] == restrict_keyword:
            continue
        new_table.append(data[i])
    return new_table

def greaterthan(data,column_number,number):
    '''
    takes if grater than on int columns 
    '''
    new_table=[]

    for i in range(len(data)):
        if data[i][column_number] > number :
            new_table.append(data[i])
            
    return new_table

def lessthan(data,column_number,number):
    '''
    takes if less than on int columns 
    '''
    new_table=[]

    for i in range(len(data)):
        if data[i][column_number] < number :
            new_table.append(data[i])
            
    return new_table

def equalto(data,column_number,number):
    '''
    take if its equal to int columns 
    '''
    new_table=[]

    for i in range(len(data)):
        if data[i][column_number] == number :
            new_table.append(data[i])
    return new_table
