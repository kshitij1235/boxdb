import contextlib
from boxdb.core import reader,writer
import logging
from colorama import init , Fore , Style
from boxdb.settings import (ERRORLOGS,
INFOLOGS,
WARNINGLOGS
)
init(convert=True)

def logWarning(database,table,message):
    """
    write logs into the file
    """
    with contextlib.suppress(Exception):
        if table!=None:
            writer(WARNINGLOGS(database,table),f'WARNING:{message}\n','a')
    print(f'{Fore.YELLOW}{message}{Style.RESET_ALL}')
    logging.basicConfig(format='%(asctime)s %(message)s')

def logerror(database,table,message):
    """
    write logs into the file
    """
    with contextlib.suppress(Exception):
        if table!=None:
            writer(ERRORLOGS(database,table),f'ERROR:{message}\n','a')
    print(f'{Fore.RED}{message}{Style.RESET_ALL}')
    logging.basicConfig(format='%(asctime)s %(message)s')

def loginfo(database,table,message):
    """
    write logs into the file
    """
    with contextlib.suppress(Exception):
        if table!=None:
            writer(INFOLOGS(database,table),f'SUCCESS:{message}\n','a')
    print(f'{Fore.GREEN}{message}{Style.RESET_ALL}')
    logging.basicConfig(format='%(asctime)s %(message)s')

def showlogs(database,table,
            error=False,
            warnings=False,
            info=False):
    """
    display log file in Terminal
    """
    if error:
        print(f"{Fore.RED}['ERROR']")
        print(reader(ERRORLOGS(database,table)))
    if warnings:
        print(f"{Fore.YELLOW}[WARNING]")
        print(reader(WARNINGLOGS(database,table)))
    if info:
        print(f"{Fore.GREEN}['SUCCESS']")
        print(reader(INFOLOGS(database,table)))
    print(Style.RESET_ALL)
