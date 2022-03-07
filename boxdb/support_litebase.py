'''
boxdb/support_litebase -> v0.3

This file contain code for
1)get the data from file, and get row data

'''

def get_content(context, target):
    """
    It gets the content from any file with
    data in it(auto generated) and returns in list
    """
    lines = []
    filtured = []
    try:
        with open(target,encoding='UTF-8') as file:
            for line in file:
                line = line.strip()
                lines.append(line)
        filtured.extend(
            elements for elements in lines if elements not in ["", " "])
    except FileNotFoundError:
        print(f"{context} file missing")
    return filtured


def get_rows(table_name):
    """
    It gets the name of the rows
    """
    return get_content("row", f"{table_name}/{table_name}_data.txt")
