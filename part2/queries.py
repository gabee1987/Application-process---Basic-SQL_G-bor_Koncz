'''
    Application process - SQL part 2 assaignment
    queries module
    Contain the queries, saved to variables.
    by Gabor Koncz
'''

mentors_query = """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country\
                                FROM mentors\
                                INNER JOIN schools\
                                ON mentors.city=schools.city\
                                ORDER BY mentors.id;"""


all_school_query = """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country\
                        FROM mentors\
                        RIGHT OUTER JOIN schools\
                        ON mentors.city=schools.city\
                        ORDER BY mentors.id;"""


mentors_by_country_query = """SELECT schools.country,\
                                COUNT(mentors.id) AS Number_of_mentors\
                                FROM mentors\
                                LEFT JOIN schools\
                                ON mentors.city=schools.city\
                                GROUP BY country;"""

