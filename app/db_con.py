'''driver for interacting with PostgreSQL from the Python scripting language'''
import os

import psycopg2 as p
import psycopg2.extras

test_url = "dbname='test_ireporter' host='localhost' port='5432' user='postgres' password='bssc4344'"
url = os.getenv('DATABASE_URL',test_url )

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
    con = connection(test_url)
    curr = con.cursor()
    users = "DROP TABLE IF EXISTS users CASCADE"
    incidents = "DROP TABLE IF EXISTS incidents CASCADE"
    queries = [incidents, users]
    try:
        for query in queries:
            curr.execute(query)
        con.commit()
        print('Destroying tables...Done ')
    except:
        print("Failed to Destroy tables")


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


def test_user_admin():
    user_admin = {
        "first_name": "john",
        "last_name": "doe",
        "email": "johndoe@example.com",
        "phone": "0708767676",
        "isAdmin": True,
        "date_created": "Thu, 13 Dec 2018 21:00:00 GMT",
        "password": "pbkdf2:sha256:50000$OwVe1ERR$ccdcf27b466c87f3fdf581183693536651e0dd8094c68d281b224375addcba3d"


    }
    query = """INSERT INTO users (first_name,last_name,email,phone,password,isAdmin,date_created) VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}');""".format(
        user_admin['first_name'], user_admin['last_name'], user_admin['email'], user_admin['phone'], user_admin['password'], user_admin['isAdmin'], user_admin['date_created'])
    conn = connection(url)
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        print('super admin created')
    except:
        return "user already exists"


def test_intervention():
    incident = {
        "createdBy": 1,
        "type": "intervention",
        "location": "66, 12",
        "status": "draft",
        "title": "NYS scandal",
        "comment": "act soon",
        "createdon": "Thu, 13 Dec 2018 14:31:20 GMT"
    }
    query = """INSERT INTO incidents (createdBy,type,location,status,title,comment,createdon) VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}');""".format(
        incident['createdBy'], incident['type'], incident['location'], incident['status'], incident['title'], incident['comment'], incident['createdon'])
    conn = connection(url)
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        print('test intervention created')
    except:
        return "test intervention already exists"


def test_redflag():
    incident = {
        "createdBy": 1,
        "type": "redflag",
        "location": "66, 13",
        "status": "draft",
        "title": "NYS scandal",
        "comment": "act soon",
        "createdon": "Thu, 13 Dec 2018 14:31:20 GMT"


    }
    query = """INSERT INTO incidents (createdBy,type,location,status,title,comment,createdon) VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}');""".format(
        incident['createdBy'], incident['type'], incident['location'], incident['status'], incident['title'], incident['comment'], incident['createdon'])
    conn = connection(url)
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        print('test redflag created')
    except:
        return "test redflag already exists"
