import contextlib
from filemod import reader
import logging
from filemod import writer
from colorama import init
from colorama import Fore
from boxdb.settings import (ERRORLOGS,
INFOLOGS,
WARNINGLOGS
)
init()

def logWarning(table,message):
    """
    write logs into the file
    """
    with contextlib.suppress(Exception):
        writer(WARNINGLOGS(table),f'WARNING:{message}\n','a')
    print(f'{Fore.YELLOW}{message}')
    logging.basicConfig(format='%(asctime)s %(message)s')

def logerror(table,message):
    """
    write logs into the file
    """
    with contextlib.suppress(Exception):
        writer(ERRORLOGS(table),f'ERROR:{message}\n','a')
    print(f'{Fore.RED}{message}')
    logging.basicConfig(format='%(asctime)s %(message)s')

def loginfo(table,message):
    """
    write logs into the file
    """
    with contextlib.suppress(Exception):
        writer(INFOLOGS(table),f'SUCCESS:{message}\n','a')

    print(f'{Fore.GREEN}{message}')
    logging.basicConfig(format='%(asctime)s %(message)s')


def showlogs(table,
            error=False,
            warnings=False,
            info=False):
    """
    display log file in Terminal
    """
    if error:
        print(f"{Fore.RED}['ERROR']")
        print(reader(ERRORLOGS(table)))
    if warnings:
        print(f"{Fore.YELLOW}[WARNING]")
        print(reader(WARNINGLOGS(table)))
    if info:
        print(f"{Fore.GREEN}['SUCCESS']")
        print(reader(INFOLOGS(table)))
