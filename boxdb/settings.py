'''
boxdb/settings.py -> v0.9

This file contain code for
1)all the paths for primary key , not null n unique

'''
DATABASE_META=lambda database : f"./{database}/{database}_META.txt"
DATABASE_TABLE=lambda database : f"./{database}/{database}_TABLE.txt"

TABLE=lambda database,table:f"./{database}/{table}"
TABLE_METADATA=lambda database,table:f"./{database}/{table}/{table}_meta.txt"

PRIMARY_KEY=lambda database,table:f'./{database}/{table}/flags/primary_key.txt'
NOT_NULL=lambda database,table:f'./{database}/{table}/flags/not_null.txt'
UNIQUE=lambda database,table:f'./{database}/{table}/flags/unique.txt'
FORBIDDEN_COLUMNS=lambda database,table :f'./{database}/{table}/flags/forbidden.txt'

ERRORLOGS=lambda database,table:  f'./{database}/{table}/logs/error.log'
INFOLOGS=lambda database,table:   f'./{database}/{table}/logs/info.log'
WARNINGLOGS=lambda database,table:f'./{database}/{table}/logs/warning.log'

COLUMNS=lambda database,table,column:f"./{database}/{table}/tables/{column}.txt"
COLUMNS_DATA=lambda database,table:f"./{database}/{table}/{table}_data.txt"
VIEW = lambda database,view : f"./{database}/{view}.txt"

FORBIDDEN_WORDS=lambda database,table,column:f"./{database}/{table}/forbiden/{column}_f.txt"

ENC_KEY=lambda database,table:f"{database}/{table}/{table}_key.key"

