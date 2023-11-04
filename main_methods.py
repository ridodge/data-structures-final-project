import students
import students_linked_list_queue
import create_db
from random import randint as r


def create_new_student(database, first_name, last_name):
    # minimum and maximum of 6-Digit ID
    minimum_id = 100000
    maximum_id = 999999
    # get random 6 digit number as student_id
    student_id = r(minimum_id, maximum_id)
    # test if student id already exists
    test = create_db.exists_student(database, student_id)
    # until a unused student ID is found, get new id
    while test is not None:
        student_id = r(minimum_id, maximum_id)
    # insert student into database with first_name, last_name, and random student_id
    create_db.insert_student(database, first_name, last_name, student_id)

def create_new_assignment(database, assignment_name):
    # minimum and maximum of 6-Digit ID
    minimum_id = 100000
    maximum_id = 999999
    # get random 6 digit number as assignment_id
    assignment_id = r(minimum_id, maximum_id)
    # test if assignment_id already exists
    test = create_db.exists_assignment(database, assignment_id)
    # until a unused assignment_id is found, get new id
    while test is not None:
       assignment_id = r(minimum_id, maximum_id)
    # insert assignment into database with name and assignment_id
    create_db.insert_student(database, assignment_id)
