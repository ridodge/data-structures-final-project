import sqlite3
from sqlite3 import Error


def create_connection(db):
    """ Connect to a SQLite database"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None


def create_table(conn, sql_create_table):
    """Creates table by name from other method"""
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)


def create_student_table(database):
    """Create student table"""
    sql_create_student_table = """CREATE TABLE IF NOT EXISTS students (
                                    student_id integer PRIMARY KEY,
                                    first_name text NOT NULL,
                                    last_name text NOT NULL
                                );"""

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create student table
        create_table(conn, sql_create_student_table)
    else:
        print("Unable to connect to " + str(database))


def create_assignment_table(database):
    """Create assignment table"""
    sql_create_student_table = """CREATE TABLE IF NOT EXISTS assignments (
                                    assignment_id integer,
                                    student_id integer NOT NULL,
                                    assignment_name text NOT NULL,
                                    possible integer NOT NULL,
                                    actual integer NOT NULL,
                                    FOREIGN KEY (student_id) REFERENCES students (id)
                                );"""

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create student table
        create_table(conn, sql_create_student_table)
    else:
        print("Unable to connect to " + str(database))


def insert_student(db, first, last):
    """Create a new student for table"""
    conn = create_connection(db)
    sql = ''' INSERT INTO students(first_name,last_name)
              VALUES(?,?) '''
    with conn:
        cur = conn.cursor()  # cursor object
        student = (first, last)
        cur.execute(sql, student)
        return cur.lastrowid # returns the row id of the cursor object


def insert_assignment(db, student_id, assignment_name, possible, actual):
    """Create a new assignment for table assignments"""
    conn = create_connection(db)
    sql = ''' INSERT INTO assignments(student_id, assignment_name, possible, actual)
              VALUES(?,?,?,?) '''
    with conn:
        cur = conn.cursor()  # cursor object
        cur.execute(sql, (student_id, assignment_name, possible, actual))
        return cur.lastrowid # returns the row id of the cursor object


def select_student(db, student_id):
    """Select all students from assignments table by student_id"""
    conn = create_connection(db)
    sql = ''' SELECT * FROM students WHERE id = ?'''
    with conn:
        cur = conn.cursor()  # cursor object
        cur.execute(sql, (student_id,))
        return cur.fetchall() # returns the row id of the cursor object


def select_assignment(db, assignment_id):
    """Select all assignments from assignments table by assignment_id"""
    conn = create_connection(db)
    sql = ''' SELECT * FROM assignments WHERE assignment_id = ?'''
    with conn:
        cur = conn.cursor()  # cursor object
        cur.execute(sql, (assignment_id,))
        return cur.fetchall() # returns the row id of the cursor object


def select_all_assignments(db):
    """Select all students from assignments table"""
    conn = create_connection(db)
    sql = ''' SELECT * FROM assignments'''
    with conn:
        cur = conn.cursor()  # cursor object
        cur.execute(sql)
        return cur.fetchall() # returns all assignments


def select_all_students(db):
    """Select all assignments from students table"""
    conn = create_connection(db)
    sql = ''' SELECT * FROM students'''
    with conn:
        cur = conn.cursor()  # cursor object
        cur.execute(sql)
        return cur.fetchall() # returns all assignments
