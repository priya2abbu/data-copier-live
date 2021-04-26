import os

DB_DETAILS = {
    'dev' : {
        'SOURCE_DB': {
            'DB_TYPE': 'my_sql',
            'DB_HOST': 'localhost',
            'DB_NAME':'retail_db',
            'DB_USER': 'retail_user',
            'DB_PASS':'itversity'
        },
        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': 'localhost',
            'DB_NAME': 'retail_db',
            'DB_USER': 'retail_user',
            'DB_PASS': 'itversity'
        }
    }
}

#import os
#
#DB_DETAILS = {
#    'dev' : {
#        'SOURCE_DB': {
#            'DB_TYPE': 'my_sql',
#            'DB_HOST': 'localhost',
#            'DB_NAME':os.environ.get('DB_NAME'),
#            'DB_USER': os.environ.get('DB_USER'),
#            'DB_PASS':'itversity'
#        },
#        'TARGET_DB': {
#            'DB_TYPE': 'postgres',
#            'DB_HOST': 'localhost',
#            'DB_NAME': 'retail_db',
#            'DB_USER': 'retail_user',
#            'DB_PASS': 'itversity'
#        }
#    }
#}