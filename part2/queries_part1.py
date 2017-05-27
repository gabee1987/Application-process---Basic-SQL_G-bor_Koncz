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

new_applicant_insert_query = """INSERT INTO applicants\
                            (first_name, last_name, phone_number, email, application_code)\
                            VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', '54823');"""

new_applicant_query = """SELECT * FROM applicants\
                            WHERE application_code='54823';"""

new_applicant_delete_query = """DELETE FROM applicants WHERE application_code = '54823';"""

jemimas_new_phone_number_update_query = """UPDATE applicants\
                                            SET phone_number = '003670/223-7459'\
                                            WHERE first_name='Jemima' AND last_name='Foreman'"""

jemimas_new_phone_number_query = """SELECT first_name || ' ' || last_name, phone_number\
                                    FROM applicants\
                                    WHERE first_name='Jemima' AND last_name='Foreman';"""

application_cancel_delete_query = """DELETE FROM applicants_mentors\
                                        WHERE applicant_id IN (SELECT id FROM applicants WHERE email LIKE '%@mauriseu.net');"""

application_cancel_delete_query2 = """DELETE FROM applicants\
                                        WHERE email LIKE '%@mauriseu.net';"""

application_cancel_reinsert_query = """INSERT INTO applicants\
                                        (first_name, last_name, phone_number, email, application_code)\
                                        VALUES ('Bill', 'Gates', '006404/640-6464', 'microsoft@mauriseu.net', '64640');"""


