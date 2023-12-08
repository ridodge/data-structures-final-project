import unittest
from students import Student

class StudentsTest(unittest.TestCase):
        def setUp(self) -> None:
                self.actual_without_next = Student(123, "First", "Last")
                self.actual_with_next = Student(1234, "First", "Last", self.actual_without_next)

        def tearDown(self) -> None:
                del self.actual_with_next
                del self.actual_without_next


        def test_creation_without_next(self):
                self.assertEqual((123, "First", "Last", None, None), self.actual_without_next.student)

        def test_student_get_first(self):
                self.assertEqual("First", self.actual_without_next.first)

        def test_student_get_last(self):
                self.assertEqual("Last", self.actual_without_next.last)

        def test_set_first(self):
                self.actual_with_next.first = "Not First"
                self.assertEqual("Not First", self.actual_with_next.first)

        def test_set_last(self):
                self.actual_with_next.last = "Not Last"
                self.assertEqual("Not Last", self.actual_with_next.last)

        def test_set_overall(self):
                self.actual_with_next.overall_grade = 1
                self.assertEqual(1, self.actual_with_next.overall_grade)

        def test_get_overall(self):
                self.assertEqual(None, self.actual_with_next.overall_grade)

