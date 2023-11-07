class StudentsLinkedQueue:
    """Students based linked list queue class that is compatible with Student class"""
    def __init__(self, first_student=None):
        self.first = first_student

    def is_empty(self):
        """Test if queue empty"""
        if not self.first:
            return True
        else:
            return False

    def enqueue(self, student):
        """Enqueue new student node"""
        # if not empty
        if not self.is_empty():
            # node starts as first in list
            node = self.first
            # while the nodes next value is not None
            while node.next is not None:
                # set new node
                node = node.next
            # when node.next is None, set node.next to student
            node.next = student
        else:
            # if empty, set student as start of list.
            self.first = student

    def dequeue(self):
        """Remove next student in queue"""
        if self.is_empty():
            # if empty, return none
            return
        else:
            # if no next value for self.first, set to none
            if not self.first.next:
                self.first = None
            else:
                # if self.next exists, set to next value
                self.first = self.first.next

    def get_students(self):
        # create empty list
        student_list = []
        # if not empty
        if not self.is_empty():
            # set node to self.first, and append to list
            node = self.first
            student_list.append(node)
            # while there is a next value
            while node.next:
                # get next value
                node = node.next
                # append next value
                student_list.append(node)
        # return list, if no self.first - returns empty list
        return student_list

    def get_next_student(self):
        if not self.is_empty():
            return self.first
