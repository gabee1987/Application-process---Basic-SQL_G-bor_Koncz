'''
    Application process - SQL part 2 assaignment
    database handler module
    by Gabor Koncz
'''

import psycopg2
from db_login_config import *


def query_manager(query, return_data='all_data'):
    '''
        Sets connection with the database and execute the queries.
        Decides which kind of data need to be returned.
    '''
    connect_str = 'dbname={0} user={1} password={2} host={3}'.format(DATABASE, USER, PASSWORD, HOST)
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(query)

    if return_data == 'all_data':
        data_from_query = cursor.fetchall()
        conn.close()
        list_of_data = [list(element) for element in data_from_query]
        return list_of_data
    elif return_data == 'one_data':
        data_from_query = cursor.fetchone()
        conn.close()
        data = data_from_query[0]
        return data
    elif return_data == 'no_data':
        conn.close()



'''def write_to_database(query):
    
        Sets connection with the database and execute the queries.
        Only usable if no data need to be returned.
    
    connect_str = 'dbname={0} user={1} password={2} host={3}'.format(DATABASE, USER, PASSWORD, HOST)
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(query)
    conn.close()
'''


