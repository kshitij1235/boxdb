'''
boxdb/settings.py -> v0.9

This file contain code for
1)all the paths for primary key , not null n unique

'''

PRIMARY_KEY=lambda table:f'./{table}/flags/primary_key.txt'
NOT_NULL=lambda table:f'./{table}/flags/not_null.txt'
UNIQUE=lambda table:f'./{table}/flags/unique.txt'
FORBIDDEN_COLUMNS=lambda table :f'./{table}/flags/forbidden.txt'

# ERRORLOGS='/logs/error.log'
ERRORLOGS=lambda table:f'./{table}/logs/error.log'
INFOLOGS=lambda table:f'./{table}/logs/info.log'
WARNINGLOGS=lambda table:f'./{table}/logs/warning.log'

COLUMNS=lambda table,column:f"./{table}/tables/{column}.txt"

FORBIDDEN_WORDS=lambda table,column:f"./{table}/forbiden/{column}_f.txt"
