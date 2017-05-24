'''
    Application process - SQL part 2 assaignment
    queries module
    by Gabor Koncz
'''

import psycopg2

mentors_and_shools_query = """SELECT mentors.first_name || ' ' || mentors.last_name AS mentor_name, schools.name, schools.country\
                                FROM mentors\
                                INNER JOIN schools\
                                ON mentors.city=schools.city\
                                ORDER BY mentors.id;"""


all_school_query = """SELECT mentors.first_name || ' ' || mentors.last_name AS mentor_name, schools.name, schools.country\
                        FROM mentors\
                        RIGHT OUTER JOIN schools\
                        ON mentors.city=schools.city\
                        ORDER BY mentors.id;"""
