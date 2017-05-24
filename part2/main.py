'''
    Application process - SQL part 2 assaignment
    main module
    by Gabor Koncz
'''

from flask import Flask, request, render_template, redirect
import psycopg2
from database_handler import query_manager
from queries import *


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    '''
        Displays the main page, where the user can
        select the queries.
    '''
    return render_template('index.html')


@app.route('/mentors')
def mentors():
    '''
        Displays the /mentors page.
        Shows the data as a table.
    '''
    table_headers = [
                    'Mentor name',
                    'School name',
                    'Country'
                    ]
    query = mentors_and_shools_query
    mentors_data = query_manager(query, 'all_data')
    return render_template('mentors.html', table_headers=table_headers, mentors_data=mentors_data)


@app.route('/all-school')
def all_school():
    '''
        Displays the /all-school page.
        Shows the data as a table.
    '''
    table_headers = [
                    'Mentor name',
                    'School name',
                    'Country'
                    ]
    query = all_school_query
    all_school_data = query_manager(query, 'all_data')
    return render_template('all-school.html', table_headers=table_headers, all_school_data=all_school_data)


if __name__ == '__main__':
    app.run(debug=True)