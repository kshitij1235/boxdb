from cryptography.fernet import Fernet
from boxdb.core import reader,byte_reader



def Encrypt_text(text,key):
    """
    This is used to encrypt a text
    """
    fernet = Fernet(key)
    return fernet.encrypt(text.encode())

def Decrypt_text(text , key):
    """
    It is used to decrypt a text
    """
    fernet = Fernet(key)
    return fernet.decrypt(text).decode()

def Encrypt_file(filename,key='auto'):
    """
    This is used to Encrypt a file 
    """
    if key =="auto":
        key = Fernet.generate_key()
    fernet = Fernet(key)
    original=byte_reader(filename)
    print(type(original))
    # encrypting the file
    encrypted = fernet.encrypt(original)

    # opening the file in write mode and
    # writing the encrypted data
    with open(filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def Decrypt_file(filename,key='auto'):
    """
    THis is used to decrypt a file
    """
    if key =="auto":
        key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted=byte_reader(filename)
    decrypted = fernet.decrypt(encrypted)

    with open(filename, 'wb') as encrypted_file:
        encrypted_file.write(decrypted)


def generate_filekey(location=None):
    """
    This is used to generate a keyfile
    """
    key = Fernet.generate_key()
    if location is None:
        with open('filekey.key', 'wb') as filekey:
           filekey.write(key)
    else:
        with open(location, 'wb') as filekey:
           filekey.write(key)
           
def get_filekey(filename):
    """
    This is used to get a key file in byte format
    """
    return byte_reader(filename)