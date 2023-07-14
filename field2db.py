import pandas as pd


data = pd.read_csv(r'./raw/jvm2008-results-20230523-015714.csv')


def str2db(data, eps):
    dtypes = data.dtypes
    ddl = ''
    for col in dtypes.index:
        col_type = str(dtypes[col])
        ddl += col.replace(' ', '_').lower()
        if col_type.startswith('float'):
            _type = 'double'
        elif col_type.startswith('int'):
            if data[col].max() < 200:
                _type = 'tinyint'
            elif data[col].max() < 1e8:
                _type = 'int'
            else:
                _type = 'bigint'
        elif col_type == 'object':
            max_len = max(data[col].apply(lambda x: len(x) if isinstance(x, str) else 0))
            if max_len < 8 - eps:
                _type = 'varchar(8)'
            elif 8 <= max_len < 16 - eps:
                _type = 'varchar(16)'
            elif 16 <= max_len < 32 - eps:
                _type = 'varchar(32)'
            elif 32 <= max_len < 64 - eps:
                _type = 'varchar(64)'
            elif 64 <= max_len < 128 - eps:
                _type = 'varchar(128)'
            elif 128 <= max_len < 256 - eps:
                _type = 'varchar(256)'
            elif 256 <= max_len < 512 - eps:
                _type = 'varchar(512)'
            else:
                _type = 'text'
                
        ddl += (' ' + _type + ',\n')
    return ddl
    

ddl = str2db(data, eps=2)