#! /usr/bin/env python3

# importing psycopg2 module to connect to the database
import psycopg2

# Giving name to database to easily refer to it by using variable name
DBNAME = "news"

# query for What are the most popular three articles of all time?
query1 = "select title, views from article_views limit 3;"

# query for Who are the most popular article authors of all time?
query2 = "select name, SUM(views) as viewers" \
         " from author_viewers group by name order by viewers desc"

# query for On which days did more than 1% of requests lead to errors?
query3 = "select date, errors from percent_errors where errors>1;"

# creating dictionaries to store result and ttile for each query asked
query_1_result = dict()
query_1_result['title'] = "Most popular articles with number of views:\n"

query_2_result = dict()
query_2_result['title'] = "Most popular authors with number of views:\n"

query_3_result = dict()
query_3_result['title'] = "Date(YYYY-MM-DD) when error more than 1% errors"


# function to return the result of the query
def get_query_result(query):
    """
        get_query_result:  function to return the result of SQL query
        Args:
            query(type : text) : stores SQL query as a text
        returns:
            return the result of query asked
    """
    try:
        db = psycopg2.connect(dbname=DBNAME)
        c = db.cursor()
    except:
        print('Error while connecting with the database')
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


# function to print the query result in the desired manner
def print_query_results(query_result):
    """
        print_query_results: function to print the query result as required
        Args:
            query_result : stores output after running the query
        returns:
            print the result in required manner
    """
    print(query_result['title'])
    for result in query_result['results']:
        print ('\t' + str(result[0]) + ' -> ' + str(result[1]) + ' views')
    print('\n')


# function to print the query result in the desired manner
def print_query_error_results(query_result):
    """
        print_query_results: function to print the query result as required
        Args:
            query_result : stores output after running the query
        returns:
            print the result in required manner
    """
    print(query_result['title'])
    for result in query_result['results']:
        print('\t' + str(result[0]) + ' -> ' + str(result[1]) + '% errors')
    print('\n')


if __name__ == '__main__':

    # calling functions to get query results, store in the dedicated dictionary
    query_1_result['results'] = get_query_result(query1)
    query_2_result['results'] = get_query_result(query2)
    query_3_result['results'] = get_query_result(query3)

    # calling the functions to get the result printed in the desired manner
    print_query_results(query_1_result)
    print_query_results(query_2_result)
    print_query_error_results(query_3_result)
