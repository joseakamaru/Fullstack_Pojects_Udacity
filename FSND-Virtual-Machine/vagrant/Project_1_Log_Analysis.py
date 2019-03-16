#Imports:
import psycopg2

DBNAME = "news"

#List of queries:
query_0_1 = "select author from articles;"
query_0_2 = "select * from authors;"
query_0_3 = "select title, name from articles join authors on articles.author = authors.id;"
query_0_4 = "select path, count(*) as views from log where path like'%article%' and status like '2%' group by path order by views desc;"
query_0_5 = "select substring(path from 10) as slug, count(*) as views from log where path like'%article%' and status like '2%' group by path order by views desc;"
query_0_6 = "select title, views, author from articles ,(select substring(path from 10) as slug , count(*) as views from log where path like '%article%' and status like '2%' group by path ) as viewtab where articles.slug = viewtab.slug;"
query_0_7 = "select date(time) as date, count(*) as error from log where status like '4%' group by date(time), status order by date(time);"
query_0_8 = "select date(time) as date, count(*) as total from log group by date(time);"

#Functions:
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

#1. What are the most popular three articles of all time? Which articles have
#been accessed the most? Present this information as a sorted list with the
#most popular article at the top.

#2. Who are the most popular article authors of all time? That is, when you sum
#up all of the articles each author has written, which authors get the most page
#views? Present this as a sorted list with the most popular author at the top.

#3. On which days did more than 1% of requests lead to errors? The log table
#includes a column status that indicates the HTTP status code that the news
#site sent to the user's browser.

if __name__ == "__main__":
    object_2 = execute_posts(query_2)
    print_results(object_2)

"""
create view topfive as select species, count(*) as num
  from animals
  group by species
  order by num desc
  limit 5;


-- Don't change the statement below!  It's there to test the view.

select * from topfive;
"""
