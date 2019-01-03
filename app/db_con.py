'''driver for interacting with PostgreSQL from the Python scripting language'''
import os

import psycopg2 as p
import psycopg2.extras
from werkzeug.security import generate_password_hash

DATABASE_URL = os.getenv('DATABASE_URL')
DATABASE_URL_TEST = os.getenv('DATABASE_URL_TEST')

def connection(url):
    con = p.connect(DATABASE_URL)
    return con

def create_tables():
    '''A database cursor is an object that points to a
    place in the database where we want to create, read,
    update, or delete data.'''
    con = connection(DATABASE_URL)
    curr = con.cursor()
    queries = tables()

    for query in queries:
        curr.execute(query)
    con.commit()


def destroy_tables():
    con = connection(DATABASE_URL)
    curr = con.cursor()
    users = "DROP TABLE IF EXISTS users CASCADE"
    incidents = "DROP TABLE IF EXISTS incidents CASCADE"
    queries = [incidents, users]
    try:
        for query in queries:
            curr.execute(query)
        con.commit()
        print('Destroying test tables...Done ')
    except:
        print("Failed to Destroy tables")


def tables():
    tbl1 = """CREATE TABLE IF NOT EXISTS incidents (
	    incidents_id serial PRIMARY KEY NOT NULL,
        createdOn TIMESTAMP,
	    type character (64) NOT NULL,
	    title  character (64) NOT NULL,
	    location character(64) NOT NULL,
        Images VARCHAR(500) NULL,
	    status character (64) NOT NULL,
	    comment character (1000) NOT NULL,
        createdBy INT NOT NULL
	    )"""

    tbl2 = """create table IF NOT EXISTS users (
     user_id serial PRIMARY KEY NOT NULL,
     first_name character(50) NOT NULL,
     last_name character(50),
     email varchar(50) NOT NULL,
     phone varchar(11),
     isAdmin boolean NOT NULL,  
     registered TIMESTAMP, 
     password varchar(500) NOT NULL
     )"""

    queries = [tbl1, tbl2]
    return queries


def super_user():
    password = generate_password_hash("hello123")
    user_admin = {
        "first_name": "john",
        "last_name": "doe",
        "email": "johndoe@example.com",
        "phone": "0707741793",
        "isAdmin": True,
        "registered": "Thu, 13 Dec 2018 21:00:00 GMT",
        "password": password
    }
    query = """INSERT INTO users (first_name,last_name,email,phone,password,isAdmin,registered) VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}');""".format(
        user_admin['first_name'], user_admin['last_name'], user_admin['email'], user_admin['phone'], user_admin['password'], user_admin['isAdmin'], user_admin['registered'])
    conn = connection(DATABASE_URL)
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        print('super user created')
    except:
        return "user already exists"
