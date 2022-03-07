from filemod import reader, writer
from os import mkdir, chdir


def get_detail(table_name):
    """
    saves meta data of the users
    """
    return reader(f"./{table_name}/{table_name}_meta.txt")


def create_project(info):
    """created necessary files in the dir"""
    try:
        mkdir(info['name'])
    except Exception:
        pass
    writing = ""
    keys_ = list(info.keys())
    values_ = list(info.values())
    for key, value in zip(keys_, values_):
        writing = f"{writing} {key}:{value}\n"

    # this make important folder that helps to store vitable info
    writer(f"./{info['name']}/{info['name']}_meta.txt", writing, "w")
    writer(f"./{info['name']}/{info['name']}_data.txt", "", "w")

    # this stores all the table data
    chdir(f"./{info['name']}")
    mkdir("tables")
