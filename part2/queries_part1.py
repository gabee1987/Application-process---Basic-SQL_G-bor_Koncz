'''
    Application process - SQL part 2 assignment
    queries module
    Contain the queries from last SI week's assignment, saved to variables.
    by Gabor Koncz
'''

mentors_all_query = """SELECT *\
                        FROM mentors\
                        ORDER BY first_name ASC;"""

applicants_all_query = """SELECT *\
                            FROM applicants\
                            ORDER BY first_name ASC;"""

name_of_mentors_query = """SELECT first_name, last_name\
                            FROM mentors;"""

nicknames_of_mentors_query = """SELECT nick_name\
                                FROM mentors\
                                WHERE city='Miskolc';"""

carols_phone_number_query = """SELECT first_name || ' ' || last_name, phone_number\
                                FROM applicants\
                                WHERE first_name='Carol';"""

real_owner_of_hat_query = """SELECT first_name || ' ' || last_name, phone_number\
                                FROM applicants\
                                WHERE email LIKE '%@adipiscingenimmi.edu';"""

