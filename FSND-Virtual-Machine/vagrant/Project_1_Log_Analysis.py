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
query_1 = "select title, views from views_table order by views desc limit 3;"
query_2 = "select name, sum(views) as views from views_table, authors where views_table.author = authors.id group by author, authors.name order by views desc;"
query_3 = "select to_char(error_table.date, 'fmmonth dd, yyyy'), (error::real/total*100)::decimal(4, 2) from error_table, total_table where error_table.date = total_table.date and (error::float/total) >= 0.01;"


 #List of views:
view_1 = "create view views_table as select title, views, author from articles ,(select substring(path from 10) as slug, count(*) as views from log where path like '%article%' and status like '2%' group by path) as viewtable where articles.slug = viewtable.slug;"
view_2 = "create view error_table as select date(time) as date, count(*) as error from log where status like '4%' group by date(time), status order by date(time);"
view_3 = "create view total_table as select date(time) as date, count(*) as total from log group by date(time);"

#Functions:
def execute_posts(query):
    """Execute posts from the 'database' base on input query."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    posts = c.fetchall()
    db.close()
    return posts

def create_view(query):
    """Creates a new view table form the 'database'."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    db.commit()
    db.close()

def print_results(object):
    for obj in object:
        print(obj)

#1. What are the most popular three articles of all time? Which articles have
#been accessed the most? Present this information as a sorted list with the
#most popular article at the top.

questions_1 = "What are the most popular three articles of all time?"

#2. Who are the most popular article authors of all time? That is, when you sum
#up all of the articles each author has written, which authors get the most page
#views? Present this as a sorted list with the most popular author at the top.

question_2 = "Who are the most popular article authors of all time?"

#3. On which days did more than 1% of requests lead to errors? The log table
#includes a column status that indicates the HTTP status code that the news
#site sent to the user's browser.

question_3 = "On which days did more than 1% of requests lead to errors?"

if __name__ == "__main__":
    #create views
    create_view(view_1)
    create_view(view_2)
    create_view(view_3)

    #Run Queries to answer questions
    execute_posts(query_1)
