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
                    'First name',
                    'Last name',
                    'School name',
                    'Country'
                    ]
    query = mentors_query
    mentors_data = query_manager(query, 'all_data')
    return render_template(
                            'mentors.html',
                            table_headers=table_headers,
                            mentors_data=mentors_data
                            )


@app.route('/all-school')
def all_school():
    '''
        Displays the /all-school page.
        Shows the datas as a table.
    '''
    table_headers = [
                    'First name',
                    'Last name',
                    'School name',
                    'Country'
                    ]
    query = all_school_query
    all_school_data = query_manager(query, 'all_data')
    return render_template(
                            'all-school.html',
                            table_headers=table_headers,
                            all_school_data=all_school_data
                            )


@app.route('/mentors-by-country')
def mentors_by_country():
    '''
        Dsiplays the /mentors-by-country page.
        Shows the datas as a table.
    '''
    table_headers = [
                    'Country',
                    'Number of mentors'
                    ]
    query = mentors_by_country_query
    mentors_by_country_data = query_manager(query, 'all_data')
    return render_template(
                            'mentors-by-country.html',
                            table_headers=table_headers,
                            mentors_by_country_data=mentors_by_country_data
                            )


@app.route('/contacts')
def contacts():
    '''
        Displays the /contacts page.
        Shows the datas as a table.
    '''
    table_headers = [
                    'School name',
                    'First name',
                    'Last name'
                    ]
    query = contacts_query
    contacts_data = query_manager(query, 'all_data')
    return render_template(
                            'contacts.html',
                            table_headers=table_headers,
                            contacts_data=contacts_data
                            )


@app.route('/applicants')
def applicants():
    '''
        Displays the /applicants page.
        Shows the datas as a table.
    '''
    table_headers = [
                    'First name',
                    'Application code',
                    'Creation date'
                    ]
    query = applicants_query
    applicants_data = query_manager(query, 'all_data')
    return render_template(
                           'applicants.html',
                           table_headers=table_headers,
                           applicants_data=applicants_data
                            )


@app.route('/applicants-and-mentors')
def applicants_and_mentors():
    '''
        Displays the /applicants-and-mentors page.
        Shows the datas as a table.
    '''
    table_headers = [
                    'First name',
                    'Application code',
                    'First name',
                    'Last name'
                    ]
    query = applicants_and_mentors_query
    applicants_and_mentors_data = query_manager(query, 'all_data')
    return render_template(
                            'applicants-and-mentors.html',
                            table_headers=table_headers,
                            applicants_and_mentors_data=applicants_and_mentors_data
                            )


if __name__ == '__main__':
    app.run(debug=True)