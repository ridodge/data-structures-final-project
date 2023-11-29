from students import Student
from students_linked_list_queue import StudentsLinkedQueue as Sq
from create_db import *
from random import randint as r


class EntryException(Exception):
    pass


def create_database(database):
    create_student_table(database)
    create_assignment_table(database)
    create_assignment_name_table(database)


def create_new_student(database, first_name, last_name):
    """Create a new student"""
    # minimum and maximum of 6-Digit ID
    minimum_id = 100000
    maximum_id = 999999
    # get random 6 digit number as student_id
    student_id = r(minimum_id, maximum_id)
    # test if student id already exists
    test = exists_student(database, student_id)
    # until an unused student ID is found, get new id
    while test is not None:
        student_id = r(minimum_id, maximum_id)
    # insert student into database with first_name, last_name, and random student_id
    insert_student(database, student_id, first_name, last_name)


def create_new_assignment_name(database, assignment_name):
    """Create a new assignment"""
    # minimum and maximum of 6-Digit ID
    minimum_id = 100000
    maximum_id = 999999
    # get random 6 digit number as assignment_id
    assignment_id = r(minimum_id, maximum_id)
    # test if assignment_id already exists
    test = exists_assignment(database, assignment_id)
    # until an unused assignment_id is found, get new id
    while test is not None:
        assignment_id = r(minimum_id, maximum_id)
    # insert assignment into database with name and assignment_id
    insert_assignment_name(database, assignment_id, assignment_name)
    return assignment_id


def test_if_students_exist(database):
    """Test if the student table is empty"""
    result = True
    if len(select_all_students(database)) == 0:
        result = False
    return result


def generate_student_linked_list(database):
    """Create linked list queue from SQL table"""
    students_list = Sq()
    # Get all students
    students = select_all_students(database)
    # define index variables
    id_index, fname_index, lname_index = 0, 1, 2
    # iterate through students
    for student in students:
        # create new student object
        new_student = Student(student[id_index], student[fname_index], student[lname_index])
        # enqueue the student object
        students_list.enqueue(new_student)
    # return linked list object
    return students_list


def check_entry(entry):
    """Check for valid characters in entry"""
    acceptable = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
    if not (acceptable.issuperset(entry)) or len(entry) == 0:
        raise EntryException


def assign_average_grades_from_linked_list(db, queue):
    """Assign average grades for students"""
    # get nect student
    node = queue.get_next_student()
    # get the assignments for that student
    assignments = select_all_assignments_by_id(db)
    grades = []
    possible = 0
    actual = 1
    i = 0
    total = 0
    # for each assignment, get the grade, and calculate average
    while i < len(assignments):
        assignment_id = assignments[i][0]
        grades.append(select_assignment_by_student(db, assignment_id, node.id)[0])
        i += 1

        if i == len(assignments):
            for grade in grades:
                total += (grade[actual]/grade[possible])
                # assign average as percentage rounded to next whole number
                average = round((total / len(grades))*100)
            node.overall_grade = average
            if node.next_student is not None:
                node = node.next_student
                i = 0




