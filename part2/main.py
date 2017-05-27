'''
    Application process - SQL part 2 assaignment
    main module
    by Gabor Koncz
'''

from flask import Flask, request, render_template, redirect
import psycopg2
from database_handler import query_manager
from queries import *
from queries_part1 import *


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


@app.errorhandler(404)
def error_hadler(error):
    return render_template('error.html')

# ==========================================================================
# Part 1 queries.
# ==========================================================================


@app.route('/index-part1')
def index_part1():
    '''
        Displays last SI weeks main page, where the user can
        select the queries.
    '''
    return render_template('index-part1.html')


@app.route('/mentors-all')
def mentors_all():
    '''
        Displays the /mentors-all page.
        Shows the data as a table.
    '''
    table_headers = [
                    'Id',
                    'First name',
                    'Last name',
                    'Nickname',
                    'Phone number',
                    'Email',
                    'City',
                    'Favourite number'
                    ]
    query = mentors_all_query
    mentors_all_data = query_manager(query, 'all_data')
    return render_template(
                            'mentors-all.html',
                            table_headers=table_headers,
                            mentors_all_data=mentors_all_data
                            )


@app.route('/applicants-all')
def applicants_all():
    '''
        Displays the /applicants-all page.
        Shows the data as a table.
    '''
    table_headers = [
                    'Id',
                    'First name',
                    'Last name',
                    'Phone number',
                    'Email',
                    'Application code'
                    ]
    query = applicants_all_query
    applicants_all_data = query_manager(query, 'all_data')
    return render_template(
                            'applicants-all.html',
                            table_headers=table_headers,
                            applicants_all_data=applicants_all_data
                            )


@app.route('/name-of-mentors')
def name_of_mentors():
    '''
        Displays the /name-of-mentors page.
        Shows the data as a table.
    '''
    table_headers = [
                    'First name',
                    'Last name'
                    ]
    query = name_of_mentors_query
    name_of_mentors_data = query_manager(query, 'all_data')
    return render_template(
                            'name-of-mentors.html',
                            table_headers=table_headers,
                            name_of_mentors_data=name_of_mentors_data
                            )


@app.route('/nicknames-of-mentors')
def nicknames_of_mentors():
    '''
        Displays the /nicknames-of-mentors page.
        Shows the data as a table.
    '''
    table_headers = [
                    'Nicknames'
                    ]
    query = nicknames_of_mentors_query
    nicknames_of_mentors_data = query_manager(query, 'all_data')
    return render_template(
                            'nicknames-of-mentors.html',
                            table_headers=table_headers,
                            nicknames_of_mentors_data=nicknames_of_mentors_data
                            )


@app.route('/carols-phone-number')
def carols_phone_number():
    '''
        Displays the /carols-phone-number page.
        Shows the data as a table.
    '''
    table_headers = [
                    'Full name',
                    'Phone number'
                    ]
    query = carols_phone_number_query
    carols_phone_number_data = query_manager(query, 'all_data')
    return render_template(
                            'carols-phone-number.html',
                            table_headers=table_headers,
                            carols_phone_number_data=carols_phone_number_data
                            )


@app.route('/real-owner-of-hat')
def real_owner_of_hat():
    '''
        Displays the /real-owner-of-hat page.
        Shows the data as a table.
    '''
    table_headers = [
                    'Full name',
                    'Phone number'
                    ]
    query = real_owner_of_hat_query
    real_owner_of_hat_data = query_manager(query, 'all_data')
    return render_template(
                            'real-owner-of-hat.html',
                            table_headers=table_headers,
                            real_owner_of_hat_data=real_owner_of_hat_data
                            )


@app.route('/new-applicant')
def new_applicant():
    '''
        Adds the new data to the database.
        Displays the /new-applicant page.
        Shows the data as a table.
    '''
    table_headers = [
                    'Id',
                    'First name',
                    'Last name',
                    'Phone number',
                    'Email',
                    'Application code'
                    ]
    query = new_applicant_insert_query
    query_manager(query, 'no_data')
    query = new_applicant_query
    new_applicant_data = query_manager(query, 'all_data')
    return render_template(
                            'new-applicant.html',
                            table_headers=table_headers,
                            new_applicant_data=new_applicant_data
                            )


@app.route('/jemimas-new-phone-number')
def jemimas_new_phone_number():
    '''
        Updates data in the database.
        Displays the /jemimas-new-phone-number page.
        Shows the data as a table.
    '''
    table_headers = [
                    'Full name',
                    'Phone number'
                    ]
    query = jemimas_new_phone_number_update_query
    query_manager(query, 'no_data')
    query = jemimas_new_phone_number_query
    jemimas_new_phone_number_data = query_manager(query, 'all_data')
    return render_template(
                            'jemimas-new-phone-number.html',
                            table_headers=table_headers,
                            jemimas_new_phone_number_data=jemimas_new_phone_number_data
                            )


@app.route('/application-cancel')
def application_cancel():
    '''
        Deletes the data from the database.
        Displays the /applicants-all page.
        Shows the data as a table.
    '''
    table_headers = [
                    'Id',
                    'First name',
                    'Last name',
                    'Phone number',
                    'Email',
                    'Application code'
                    ]
    query = application_cancel_delete_query
    query_manager(query, 'no_data')
    query = applicants_all_query
    applicants_all_data = query_manager(query, 'all_data')
    return render_template(
                            'application-cancel.html',
                            table_headers=table_headers,
                            applicants_all_data=applicants_all_data
                            )




if __name__ == '__main__':
    app.run(debug=True)