# BOXDB

This is a database management lib made for python, which works like any Libraries and is very lite
no additional setup is required but there is some procedure to create a project is very easy.

## Installation

- use `pip install boxdb`
- Make sure that your `pip` version is updated `pip install --upgrade pip`. 
- Select the correct package for your environment:
- Import the package: ``import boxdb``

### Clone the project

```bash
  git clone https://github.com/kshitij1235/boxdb/tree/main/dist
```

Install

```bash
  pip install boxdb
```

# UPDATE

- FORBIDDEN WORDS ARE ADDED TO THE COLUMN !! , so now you can restrict some words for a column.
- IT ALSO KEEPS TRACK OF TABLE WITH LOGS
- auth_details() improved speed and algorithm
- specific_auth() improved speed and algorithm
- add_row() made more faster
- drop_primary_key()->added
- assign_primary_key()->added
- get_table()->loads the table lazily now and memory efficient and faster
- internal check primary row fixed
- delete_row() -> added it deleted columns permenently
- remove_row() -> added it does not delete columns permenently
- create_column() -> added feature to create a uniques column
- create_column() -> added feature to create a column with forbident words
- solved bugs in create_project
- changes made to the core modules

----

## Libraries Used

- Tabulate
- Coloroma

## Features

- Very lite and easy to maintain.
- custom encryption is very easy to apply.
- faster in performance.

## Things to keep in mind

- you can only access the database file when your python file and database file are in the same directory

---

# Structure Of The Database

```bash
{database_name}
|
|
├─{table_name}
  │ 
  ├─ flags
  │   ├── forbidden.txt
  │   └── not_null.txt
  │   └── primary_key.txt
  │   └── unique.txt
  ├── Forbidden
  │   ├── {forbiden_column}_f.txt
  ├── Logs
  │   ├── error.log
  │   ├── info.log
  │   └── warning.log
  ├── tables
  │   ├── {columns}.txt
  ├── {table_name}_data.txt
  └── {table_name}_meta.txt
```

---

# How to use it :)

## phase 1 (Creating a TABLE)

1) In order to start with boxdb you first need to have a file for table reaction with a 
   variable with some  parameters

2) you can use this code to start with it too 

```python
from boxdb import*

#in this variable you make sure too include the the name key aka variable as it will be your table name 
# and rest you can put any number of keys values you want its upto you 

#The only important key value is name 
database_name="parent"
info={
    'name':"plasma",      
    'description':"makeing heard of cows talking to each other and making things more brigth for the world to take stem"
}

# with the help of this function your database will be created 
create_database(database_name)

# with the help of this function your table inside database will be created 
create_table(database_name,info)

#with the help of this function you can check the details of your table which  you stored
details=get_detail(database_name,"plasma")
print(details)
```

| functions      | description                                                   | arguments                                    |
| -------------- | ------------------------------------------------------------- | -------------------------------------------- |
| create_database | This function creates a  basic file system to store table info | database(database_name) |
| create_table | This function creates a  basic file system to store table info in database | database(database_name),info(patten given above for variable naming) |
| get_detail     | This gives you all the basic details of the table             | table_name                                   |

## phase 2 (wow you learned to set up boxdb)

### Now  lets start with column creation and deletion with PRIMARY KEY

```python
from boxdb import*

database_name="parent"
# At the start let's create some rows!!!!

# you can pass a string or even list to create columns according to your wish
# ill show creating 4 rows 3 with rows and 1 with string
columns=["sr no","names of cow","lites fo milk"]

# this function takes table name (in my case its  "plasma") and columns you can pass list if you have many rows 
# or you can use string if you wanna create one single row 


# this is multiple 
create_column(database_name"plasma", rows)

# this is single row  
create_column(database_name,"plasma", "update")

# you can make the primary key this way 
# and it also shows some more features it consists 

# create_column function has 3 more parameters  

# not_null -> to avoid blank spaces and null values in column 
# it takes bool values

# unique -> it is used to rest the repetitive words in the column 
# it takes bool value

# forbiden_words -> it is used to restrict sets of words in the column
# it takes a list as a parameter with some words to restrict 

create_column(database_name,"plasma",
    "id",
    primary_key=True,
    not_null=False,
    unique=False,
    Forbiden_words=None
)

#you can always delete a column if you want


# this function takes the table name (in my case its  "plasma") and columns you can pass list if you have many rows to delete
# or you can pass a sting if you wanna delete a single row

#, in this case, am deleting a single column but you can always pass a list to
remove_column(database_name"plasma", "update")
```

| functions     | description                                         | arguments                                       |
| ------------- | --------------------------------------------------- | ----------------------------------------------- |
| create_column | This function helps you create columns in you table | database_name, table_name,columns name(accepts list or string) |
| remove_column | Delete columns                                      | database_name, table_name,column(accepts list or string)       |

### Lets learn about creating rows

```python
from boxdb import*
'''
# At start lets create some rows!!!!

# you have to pass list to rows according to the columns 

# for example if you have three columns ,you have to pass 3 elements each elements gets added to 
# each row 

# In short you can add 1 row at a time but a fix for that will be release soon too '

'''
rows=["1","amanda","28","er"]

'''
# this function takes table name (in my case its  "plasma") and rows you have to  pass list 
# that you created earlier according to row size 
'''
database_name="parent"

# this is multiple 
add_row(database_name,"plasma", rows)
add_row(database_name,"plasma",["2","ana","28","3e"])
add_row(database_name,"plasma",["3","kyee","28","5e"])


#you can always delete a row if you want

# this functions takes table name (in my case its "plasma")
# rules 
# 1)it needs a primary key
# it takes the column name to change and element to change

remove_row(database_name,"plasma","id","3e")
# this fucntion takes table name (in my case its  "plasma") 
# and the number of row 

# in this case am delelting a single columns which is row number 1
remove_column_number(database_name,"plasma", 1)

#you can always update a row if you want

# it takes table name 
# and a value from primary key that should exist in same row
# it takes column number and what to update in  

update_row(database_name,"plasma","5e","update","22")
```

| functions            | description                                         | arguments                                 |
| -------------------- | --------------------------------------------------- | ----------------------------------------- |
| add_row              | This function helps you create columns in you table | database_name, table_name,column_data(list)              |
| remove_column_number | Delete row by index                                 | database_name, table_name,remove_row_number              |
| remove_row           | row that can be recovered                           | database_name, table_name,column,row_element             |
| delete_row           | remove row permently                                |                                           |
| update_row           | update values in row                                | database_name, table_name,primary_value, column, element |

### Showing table

```python
from boxdb import*

# Displaying table is a kids job, its very easy 

# this function helps you to show table 
# this function takes a single argument which is table name(in my case its "plasma")

##i understand few freatures should be added to improve the use of show table functions
# and yes it would be release soon 

get_table(database_name,"plasma")

'''
now there is another method to do it with selective rows
''' 

list_of_rows=["sr_no","number_of_cows"]
get_table(database_name,"plasma",list_of_rows)
```

| functions | description                                | arguments  |
| --------- | ------------------------------------------ | ---------- |
| get_table | This function helps to visualize the table | database_name,table_name |

## License

[MIT](https://github.com/kshitij1235/boxdb/blob/main/LICENSE)

## Feedback

If you have any feedback, please reach out to us at email kshitijjathar7@gmail.com 