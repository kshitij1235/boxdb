# BOX db


<img src="https://user-images.githubusercontent.com/65331304/151694894-c4720d7b-0535-4398-8bad-1b6b968fe672.png" width="280" height="280">

# BOXDB

This a database managment lib made for python, which works like any Libraries and is very lite
no aditional setup require but there is some procedure to create a project is very easy.

## Installation

1. use `pip install boxdb`
2. Make sure that your `pip` version is updated `pip install --upgrade pip`. 
3. Select the correct package for your environment:
4. Import the package: ``import boxdb``

### Clone the project

```bash
  git clone https://github.com/kshitij1235/boxdb/tree/main/dist
```

Install

```bash
  pip install boxdb
```

## Libraries Used

- Tabulate
- filemod


## Features

- Very lite and easy to maintain
- custom encryption are very easy to apply
- faster in performace


# How to use it :)



## phase 1 


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
boxdb.create_project(info)

#with the help of this function you can check the details of your table which  you stored
details=boxdb.get_detail("plasma")
print(details)

```



| functions         | description        | arguments |
| ----------------- | -------------------|-----------|
| create_project | This function creates basic file system to store data|info(patten given above for variable naming)|
| get_detail| This gives you all the basic details of the table |table_name|

