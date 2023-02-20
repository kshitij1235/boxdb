from re import findall
from mmap import mmap, ACCESS_READ

def _count_generator(counter_):
    while b := counter_(1024 * 1024):
        yield b

def writer(filename, content, method):
    """writes the data to the file
    just takes filename your data as content and method to open the file"""
    try:
        with open(filename, method) as file:
            file.write(content)
        file.close()
        return True
    except Exception:
        print(f"ERROR LOADING FILE {filename}")
        return False


def reader(filename):
    """Reads data and returs a all the content as
    string """
    try:
        with open(filename, mode="r", encoding="UTF-8") as file_obj:
            with mmap(file_obj.fileno(), length=0, access=ACCESS_READ) as mmap_obj:
                return mmap_obj.read().decode('UTF-8')
    except FileNotFoundError:
        print(f"ERROR LOADING FILE {filename}")

def byte_reader(filename):
    """Reads data and returs a all the content as
    string """
    try:
        with open(filename, mode="r", encoding="UTF-8") as file_obj:
            with mmap(file_obj.fileno(), length=0, access=ACCESS_READ) as mmap_obj:
                return mmap_obj.read()
    except FileNotFoundError:
        print("ERROR LOADING FILE")

def read_specific_line(filename, line):
    """reads a specific line from a file 
    just takes filename and line number"""
    try:
        with open(filename) as file:
            content = file.readlines()
            content = content[line]
        return content
    except Exception:
        return False


def extract_numbers_from(filename):
    """Returns all the numerical values as list"""
    try:
        file = reader(filename)
    except FileNotFoundError:
        print("FIle ERROR")
    temp = findall(r'\d+', file)
    return list(map(int, temp))


def remove_word(filename, excludedWord):
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        newLines = [' '.join([word for word in line.split() if word != excludedWord])
                    for line in lines]
        with open(filename, 'w') as f:
            for line in newLines:
                f.write(f"{line}\n")
        return True
    except FileNotFoundError:
        return False

def number_of_lines(filename):
    with open(filename, 'rb') as fp:
        c_generator = _count_generator(fp.raw.read)
        count = sum(buffer.count(b'\n') for buffer in c_generator)
        return count + 1


def delete_specific_line(filename, line):
    try:
        with open(filename, "r") as f:
            contents = f.readlines()
        # remove the line item from list, by line number, starts from 0
        contents.pop(line-1)

        with open(filename, "w") as f:
            contents = "".join(contents)
            f.write(contents)
        return True
    except FileNotFoundError:
        return False


def write_specific_line(filename, line, content):
    with open(filename, 'r') as file:
        data = file.readlines()
    data[line-1] = f"{content}\n"
    with open(filename, 'w') as file:
        # print(data)
        file.writelines(data)


def word_search_line(filename, word):
    with open(filename) as file:
        lines = file.readlines()
    lines = list(map(str.strip, lines))
    for line_number, line in enumerate(lines, 1):
        if word == line:
            return line_number
    return False


def word_find(filname, word):
    emp = []
    with open(filname, "r", encoding='UTF-8') as f:
        my_file = f.readlines()
        emp.extend(elements.strip() for elements in my_file)
    return word in emp


def get_limited_lines(filename,line_limit):
    line = []
    with open(filename, "r") as f:
        for _ in range(line_limit):
            line.append(f.readline())
    return line

def hide_file(filename):
    import subprocess
    subprocess.check_call(["attrib","+H",filename])