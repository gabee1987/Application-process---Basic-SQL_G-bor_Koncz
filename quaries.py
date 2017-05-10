import psycopg2
import sys
from display import *


try:
    conn_string = "host='localhost' dbname='gabee' user='gabee' password='mamalaz1'"  # our connection string
except:
    print("Unable to connect to the database")
conn = psycopg2.connect(conn_string)  # connection to the database
cur = conn.cursor()  # our cursor object to perform queries


def mentors_all():
    cur.execute("SELECT * FROM mentors")
    mentor_table = cur.fetchall()
    return mentor_table


def applicants_all():
    cur.execute("SELECT * FROM applicants ORDER BY first_name ASC")
    applicants_table = cur.fetchall()


def name_of_mentors():
    cur.execute("SELECT first_name, last_name FROM mentors")
    mentor_names = cur.fetchall()
    return mentor_names


if __name__ == '__main__':
    main()
