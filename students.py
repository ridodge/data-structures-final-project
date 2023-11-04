class Student:
    """Node class for students in classroom class"""
    def __init__(self, student_id, fname, lname, next_student=None):
        self.student_id = student_id
        self.fname = fname
        self.lname = lname
        self.next_student = next_student
        self.overall_grade = None

    @property
    def id(self):
        return self.student_id

    @id.setter
    def id(self, value):
        self.student_id = value

    @property
    def first(self):
        return self.fname

    @first.setter
    def first(self, value):
        self.fname = value

    @property
    def last(self):
        return self.lname

    @last.setter
    def last(self, value):
        self.lname = value

    @property
    def next(self):
        return self.next_student

    @next.setter
    def next(self, value):
        self.next_student = value

    @property
    def overall(self):
        return self.overall_grade

    @overall.setter
    def overall(self, value):
        self.overall_grade = value

    @property
    def student(self):
        return self.student_id, self.fname, self.lname, self.next_student, self.overall_grade


