import psycopg2
import sys


try:
    conn_string = "host='localhost' dbname='gabee' user='gabee' password='mamalaz1'"  # our connection string
except:
    print("Unable to connect to the database")
conn = psycopg2.connect(conn_string)  # connection to the database
cur = conn.cursor()  # our cursor object to perform queries


def mentors_all():
    cur.execute("SELECT * FROM mentors ORDER BY first_name ASC")
    mentor_table = cur.fetchall()
    return mentor_table


def applicants_all():
    cur.execute("SELECT * FROM applicants ORDER BY first_name ASC")
    applicants_table = cur.fetchall()
    return applicants_table


def name_of_mentors():
    cur.execute("SELECT first_name, last_name FROM mentors")
    mentor_names = cur.fetchall()
    return mentor_names


def nicknames_of_mentors():
    cur.execute("SELECT nick_name FROM mentors WHERE city='Miskolc'")
    nincknames_of_mentors = cur.fetchall()
    return nincknames_of_mentors


def carols_phone_number():
    cur.execute("SELECT first_name || ' ' || last_name, phone_number FROM applicants\
                WHERE first_name='Carol'")
    carols_phone_number = cur.fetchall()
    return carols_phone_number


if __name__ == '__main__':
    main()
