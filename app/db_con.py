'''driver for interacting with PostgreSQL from the Python scripting language'''
import os

import psycopg2 as p
import psycopg2.extras

url = "dbname='ireporter' host='localhost' port='5432' user='postgres' password='bssc4344'"
# test_url = "dbname='test_ireporter' host='localhost' port='5432' user='antonnifo' password='root123'"

# db_url = os.getenv('DATABASE_URL')


def connection(url):
    con = p.connect(url)
    print("connecting to db...connected")
    return con

def cursor(url):
    con = connection(url)
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    return cur
    
def create_tables():
    '''A database cursor is an object that points to a
    place in the database where we want to create, read,
    update, or delete data.'''
    con = connection(url)
    curr = con.cursor()
    queries = tables()

    for query in queries:
        curr.execute(query)
    con.commit()


def destroy_tables():
    con = connection(url)
    curr = con.cursor()
    users  = "DROP TABLE IF EXISTS users CASCADE"
    incidents = "DROP TABLE IF EXISTS incidents CASCADE"
    queries = [incidents, users]
    try:
        for query in queries:
            curr.execute(query)
        con.commit()
    except:
        print("Failed to Destroy tables")

# def destroy_test_tables():
#     con = connection(test_url)
#     curr = con.cursor()
#     users  = "DROP TABLE IF EXISTS users CASCADE"
#     incidents = "DROP TABLE IF EXISTS incidents CASCADE"
#     queries = [incidents, users]
#     try:
#         for query in queries:
#             curr.execute(query)
#         con.commit()
#     except:
#         print("Failed to Destroy tables")

def tables():
    tbl1 = """CREATE TABLE IF NOT EXISTS incidents (
	    incidents_id serial PRIMARY KEY NOT NULL,
	    type character (64) NOT NULL,
	    title  character (64) NOT NULL,
	    location character(64) NOT NULL,
	    status character (64) NOT NULL,
	    comment character (1000) NOT NULL,
        createdBy INT NOT NULL,
	    createdON timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
	    )"""

    tbl2 = """create table IF NOT EXISTS users (
     user_id serial PRIMARY KEY NOT NULL,
     first_name character(50) NOT NULL,
     last_name character(50),
     email varchar(50) NOT NULL UNIQUE,
     phone varchar(11),
     isAdmin boolean NOT NULL,  
     date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL, 
     password varchar(500) NOT NULL
     )"""

    queries = [tbl1, tbl2]
    return queries
