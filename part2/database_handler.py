'''
    Application process - SQL part 2 assaignment
    database handler module
    by Gabor Koncz
'''

import psycopg2
import db_login_config


def db_connection(query, query_type='all_data'):
    '''
        Sets connection with the database and execute the queries.
        Decides that need to return data or not.
    '''
    connect_str = "dbname={0} user={1} password={2} host={3}".format(DATABASE, USER, PASSWORD, HOST)
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    cursor = conn.cursor()

    if query_type == 'all_data':
        data_from_query = cursor.fetchall()
        conn.close()
        list_of_data = [list(element) for element in data_from_query]
        return list_of_data
    elif query_type == 'one_data':
        data_from_query = cursor.fetchone()
        conn.close()
        data = data_from_query[0]
        return data
