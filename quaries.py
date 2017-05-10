import psycopg2
import sys


def db_connection():
    try:
        conn_string = "host='localhost' dbname='gabee' user='gabee' password='mamalaz1'"  # our connection string
    except:
        print("Unable to connect to the database")
    conn = psycopg2.connect(conn_string)  # connection to the database
    cursor = conn.cursor()  # our cursor object to perform queries


def main():
    db_connection()


if __name__ == '__main__':
    main()
