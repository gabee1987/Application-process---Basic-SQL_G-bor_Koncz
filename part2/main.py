from flask import Flask, request, render_template, redirect
import psycopg2
import database_handler


app = Flask(__name__)


def index():
    '''
        Displays the main page, where the user can
        select the queries.
    '''
    return render_template(index.html)

if __name__ == '__main__':
    app.run(debug=True)