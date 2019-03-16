#Imports:
import psycopg2

#1. What are the most popular three articles of all time? Which articles have
#been accessed the most? Present this information as a sorted list with the
#most popular article at the top.
DBNAME = "news"

#List of queries:
query_1 = "select author from articles;"
query_2 = "select * from authors;"
query_3 = "select title, name from articles join authors on articles.author = authors.id;"

def execute_posts(query):
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    posts = c.fetchall()
    db.close()
    return posts

def print_results(object):
    for obj in object:
        print(obj)

#2. Who are the most popular article authors of all time? That is, when you sum
#up all of the articles each author has written, which authors get the most page
#views? Present this as a sorted list with the most popular author at the top.

#3. On which days did more than 1% of requests lead to errors? The log table
#includes a column status that indicates the HTTP status code that the news
#site sent to the user's browser.

if __name__ == "__main__":
    object_2 = execute_posts(query_2)
    print_results(object_2)
