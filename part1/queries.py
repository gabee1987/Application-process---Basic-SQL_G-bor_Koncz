"""
    Basic SQL assaignment database handler module
    by Gabor Koncz
"""

import psycopg2
import sys


try:
    conn_string = "host='localhost' dbname='gabee' user='gabee' password='********'"  # our connection string
except:
    print("Unable to connect to the database")
conn = psycopg2.connect(conn_string)  # connection to the database
cur = conn.cursor()  # our cursor object to perform queries


def mentors_all():  # Shows all data from mentors table
    cur.execute("""SELECT * FROM mentors ORDER BY first_name ASC;""")
    mentor_table = cur.fetchall()
    return mentor_table


def applicants_all():  # Shows all data from applicants table
    cur.execute("""SELECT * FROM applicants ORDER BY first_name ASC;""")
    applicants_table = cur.fetchall()
    return applicants_table


def name_of_mentors():  # Shows the first_name and last_name from mentors table
    cur.execute("""SELECT first_name, last_name FROM mentors;""")
    mentor_names = cur.fetchall()
    return mentor_names


def nicknames_of_mentors():  # Shows the nicknames of mentors from Miskolc
    cur.execute("""SELECT nick_name FROM mentors WHERE city='Miskolc';""")
    nincknames_of_mentors = cur.fetchall()
    return nincknames_of_mentors


def carols_phone_number():  # Shows the full_name and phone_number of the girl who lost her hat
    cur.execute("""SELECT first_name || ' ' || last_name, phone_number FROM applicants\
                WHERE first_name='Carol';""")
    carols_phone_number = cur.fetchall()
    return carols_phone_number


def real_owner_of_hat():  # Shows the full_name and phone_number of the real owner of the hat
    cur.execute("""SELECT first_name || ' ' || last_name, phone_number FROM applicants\
                WHERE email LIKE '%@adipiscingenimmi.edu';""")
    other_girl_phone_number = cur.fetchall()
    return other_girl_phone_number


def new_applicant():  # Creates and shows all the data of the new applicant
    cur.execute("""INSERT INTO applicants\
                (first_name, last_name, phone_number, email, application_code)\
                VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', '54823');""")
    cur.execute("""SELECT * FROM applicants\
                WHERE application_code='54823';""")
    new_applicant_data = cur.fetchall()
    cur.execute("""DELETE FROM applicants WHERE application_code = '54823';""")
    return new_applicant_data


def jemimas_new_phone_number():  # Updates and shows Jemima's new phone number
    cur.execute("""UPDATE applicants\
                SET phone_number = '003670/223-7459'\
                WHERE first_name='Jemima' AND last_name='Foreman'""")
    cur.execute("""SELECT first_name || ' ' || last_name, phone_number FROM applicants\
                WHERE first_name='Jemima' AND last_name='Foreman';""")
    jemimas_phone_number = cur.fetchall()
    return jemimas_phone_number


def application_cancel():  # Deletes the datas with this email domain: @mauriseu.net
    cur.execute("""DELETE FROM applicants\
                WHERE email LIKE '%@mauriseu.net';""")



