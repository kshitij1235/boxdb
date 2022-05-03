
# BOXDB

This a database managment lib made for python, which works like any Libraries and is very lite
no aditional setup require but there is some procedure to create a project is very easy.

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
- PRIMARY KEY AND AUTHENTICATE SYSTEM 
- solved bug in auth system
- solved bugs in create_project()
- auth_details() improved speed
- get_table() doesnt crash if there is not table made
- get_table() added tags for primary key
- create_columns() works better now
- update_rows() added to update row values
- remove_rows() added which work flawless with primary_key refrence    
- remove_columns() made improvements to it 
- get_content() speed optimization
- get_element() function added

----

## Libraries Used

- Tabulate
- filemod


## Features

- Very lite and easy to maintain
- custom encryption are very easy to apply
- faster in performace



## Things to keep in mind 

- you can only acess the database file when your python file and database file are in same directory

# How to use it :)



## phase 1 (Creating a TABLE)


1) In order to start with boxdb you first need to have a file for table reaction with a 
   variable with some  parameters

2) you can use this code to start with it too 


```python

from boxdb import*

#in this variable you make sure too include the the name key aka variable as it will be your table name 
# and rest you can put any number of keys values you want its upto you 

info={
    'name':"plasma",      
    'description':"makeing heard of cows talking to each other and making things more brigth for the world to take stem"
}

# with the help of this function your table will be created 
create_project(info)

#with the help of this function you can check the details of your table which  you stored
details=get_detail("plasma")
print(details)

```



| functions         | description        | arguments |
| ----------------- | -------------------|-----------|
| create_project | This function creates basic file system to store data|info(patten given above for variable naming)|
| get_detail| This gives you all the basic details of the table |table_name|


## phase 2 (wow you learned to set up boxdb)

 ### Now  lets start with column creation and deletion with PRIMARY KEY



```python

from boxdb import*

# At start lets create some row !!!!

# you can pass string or even list to create columns its according to your wish
# ill show creating 4 rows 3 with rows and 1 with string
columns=["sr no","names of cow","lites fo milk"]

# this fucntion takes table name (in my case its  "plasma") and columns you can pass list if you have many rows 
# or you can use string if you wanna create one single row 


# this is multiple 
create_column("plasma", rows)

# this is single row  
create_column("plasma", "update")

# you can make primary key this way 
create_column("plasma", "id",primary_key=True)

#you can always delete a column if you want


# this fucntion takes table name (in my case its  "plasma") and columns you can pass list if you have many rows to delete
# or you can pass a sting if you wanna delete a single row

# in this case am deleting a single column but you can always pass a list to
remove_column("plasma", "update")


```

| functions         | description        | arguments |
| ----------------- | -------------------|-----------|
|create_column| This function helps you create columns in you table|table_name,columns name(accepts list or string)|
|remove_column| Delete columns  |table_name,column(accepts list or string)|


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

# this is multiple 
add_row("plasma", rows)
add_row("plasma",["2","ana","28","3e"])
add_row("plasma",["3","kyee","28","5e"])


#you can always delete a row if you want

# this functions takes table name (in my case its "plasma")
# rules 
# 1)it needs a primary key
# it takes the column name to change and element to change

remove_row("plasma","id","3e")
# this fucntion takes table name (in my case its  "plasma") 
# and the number of row 

# in this case am delelting a single columns which is row number 1
remove_column_number("plasma", 1)

#you can always update a row if you want

# it takes table name 
# and a value from primary key that should exist in same row
# it takes column number and what to update in  

update_row("plasma","5e","update","22")


```

| functions         | description        | arguments |
| ----------------- | -------------------|-----------|
| add_row | This function helps you create columns in you table|table_name,column_data(list)|
| remove_column_number| Delete row by index |table_name,remove_row_number|
| remove_row| Delete row |table_name,column,row_element|
| update_row|update values in row |table_name,primary_value, column, element|



### Showing table


```python

from boxdb import*

# Displaying table is a kids job , its very easy 

# this function helps you to show table 
# this function takes a single argument which is table name(in my case its "plasma")

##i understand few freatures should be added to improve the use of show table functions
# and yes it would be release soon 

get_table("plasma")

'''
now there is another method to do it with selective rows
''' 

list_of_rows=["sr_no","number_of_cows"]
get_table("plasma",[list_of_rows])

```

| functions         | description        | arguments |
| ----------------- | -------------------|-----------|
| get_table| This function helps to visualize the table|table_name|


## License

[MIT](https://github.com/kshitij1235/boxdb/blob/main/LICENSE)



## Feedback
If you have any feedback, please reach out to us at email kshitijjathar7@gmail.com 

  