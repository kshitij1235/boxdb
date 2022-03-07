"""

boxdb/table_checkup.py -> v0.3

This file contain code for
1)to check table

"""
from os import path


def check_table(table_name):
    """
    checks if table exist's or not
    """
    return path.exists(f"./{table_name}")
