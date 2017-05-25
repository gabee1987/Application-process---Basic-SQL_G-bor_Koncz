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


contacts_query = """SELECT schools.name, mentors.first_name, mentors.last_name\
                    FROM schools\
                    INNER JOIN mentors\
                    ON schools.contact_person=mentors.id\
                    ORDER BY schools.name;"""


applicants_query = """SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date\
                        FROM applicants\
                        RIGHT JOIN applicants_mentors\
                        ON applicants.id=applicants_mentors.applicant_id\
                        WHERE applicants_mentors.creation_date > '2016-01-01'\
                        ORDER BY applicants_mentors.creation_date DESC;"""


applicants_and_mentors_query = """SELECT applicants.first_name, applicants.application_code,\
                                    COALESCE(mentors.first_name, 'None'),\
                                    COALESCE(mentors.last_name, 'None')\
                                    FROM applicants\
                                    LEFT JOIN applicants_mentors\
                                    ON applicants.id=applicants_mentors.applicant_id\
                                    LEFT JOIN mentors\
                                    ON applicants_mentors.mentor_id=mentors.id
                                    ORDER BY applicants.id;"""

