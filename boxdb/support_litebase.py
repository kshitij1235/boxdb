
def check_list(variable):
    return str(type(variable)) == "<class 'list'>"


def get_content(context, target):
    lines = []
    filtured = []
    try:
        with open(target) as file:
            for line in file:
                line = line.strip()
                lines.append(line)
        for elements in lines:
            if elements in ["", " "]:
                continue
            filtured.append(elements)
    except:
        print(f"{context} file missing")
    return filtured


def get_rows(table_name):
    return get_content("row", f"{table_name}/{table_name}_data.txt")
