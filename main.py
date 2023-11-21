import tkinter
from tkinter import ttk
from main_methods import *


class GradeBookGUI:
    """Interactive grade book GUI to create assignments/grades, and run reports. """
    def __init__(self):
        # Define root and design, construct root with main_menu frame
        self.root = tkinter.Tk()
        self.root.geometry("600x500")
        self.root.configure(bg="black")
        self.database = "gradebook.db"
        create_database(self.database)

        self.set_fist_canvas()
        self.root.mainloop()

    def set_fist_canvas(self):
        """Test if database has students"""
        # if no students
        if len(select_all_students(self.database)) == 0:
            # Start creating students
            self.create_students()
        # else main menu
        else:
            self.main_menu()

    def main_menu(self):
        """Main menu of grade book"""
        self.students = generate_student_linked_list(self.database)
        assign_average_grades_from_linked_list("gradebook.db", self.students)
        # Define canvas for main manu
        main_canvas = tkinter.Canvas(self.root, width=580, height=480, background='slate gray')
        main_canvas.pack(pady=10)
        # Welcome label
        welcome = tkinter.Label(text="Welcome to your grade book!", background='slate gray')
        # Button to go to generate main assignment canvas and destroy main canvas
        create_assignment_button = ttk.Button(main_canvas, text="Create Assignment", command=lambda: (main_canvas.destroy(), self.create_assignment()))
        main_canvas.create_window(290, 50, window=welcome)
        main_canvas.create_window(290, 100, window=create_assignment_button)
        # Run GUI
        self.root.mainloop()

    def create_assignment(self):
        """Create assignment menu of grade book"""
        # Define create assignment menu
        new_assignment_canvas = tkinter.Canvas(self.root, width=580, height=480, background='slate gray')
        new_assignment_canvas.pack(pady=10)
        # Informative label to guide user
        information = tkinter.Label(text="Create a new assignment:", background='slate gray')
        points_label = tkinter.Label(text="Possible points:", background='slate gray')
        # Entry point for assignment
        assignment_entry = ttk.Entry(new_assignment_canvas)
        points_entry = ttk.Entry(new_assignment_canvas)
        # Continue button
        continue_button = ttk.Button(new_assignment_canvas, text="Continue", command=lambda: (create(assignment_entry.get())))
        # Exit assignment creation menu, return to main menu
        exit_button = ttk.Button(new_assignment_canvas, text="Main Menu", command=lambda: (new_assignment_canvas.destroy(), self.main_menu()))
        new_assignment_canvas.create_window(210, 50, window=information)
        new_assignment_canvas.create_window(370, 50, window=points_label)
        new_assignment_canvas.create_window(210, 100, window=assignment_entry)
        new_assignment_canvas.create_window(370, 100, window=points_entry)
        new_assignment_canvas.create_window(340, 150, window=continue_button)
        new_assignment_canvas.create_window(240, 150, window=exit_button)

        def create(name):
            try:
                # Test input
                check_entry(name)
                points = int(points_entry.get())
            # Catch exceptions and create error screen
            except (EntryException, ValueError):
                error_information = tkinter.Label(text="Invalid Entry. Please check your input.", background='slate gray')
                error_button = ttk.Button(new_assignment_canvas, text="OK", command=lambda: (error_information.destroy(), error_button.destroy()))
                new_assignment_canvas.create_window(290, 300, window=error_information)
                new_assignment_canvas.create_window(290, 400, window=error_button)
            # Else create assignment and add to database, destroy screen, send to grading screen
            else:
                assignment_num = create_new_assignment_name(self.database, name)
                new_assignment_canvas.destroy()
                self.grading(assignment_num, points)

    def create_students(self):
        """Create assignment menu of grade book"""
        # Define create student menu
        new_student_canvas = tkinter.Canvas(self.root, width=580, height=480, background='slate gray')
        new_student_canvas.pack(pady=10)
        # Informative label to guide user
        information = tkinter.Label(text="Create a new student:", background='slate gray')
        fname = tkinter.Label(text="First Name:", background='slate gray')
        lname = tkinter.Label(text="Last Name:", background='slate gray')
        # Entry point for student first name
        first_entry = ttk.Entry(new_student_canvas)
        # Entry point for student first name
        last_entry = ttk.Entry(new_student_canvas)
        # Continue button
        continue_button = ttk.Button(new_student_canvas, text="Save - Next Student", command=lambda: (attempt(first_entry.get(), last_entry.get())))
        # Exit student creation menu, return to main menu
        exit_button = ttk.Button(new_student_canvas, text="Exit", command=lambda: (new_student_canvas.destroy(), self.main_menu()))
        new_student_canvas.create_window(290, 50, window=information)
        new_student_canvas.create_window(210, 75, window=fname)
        new_student_canvas.create_window(370, 75, window=lname)
        new_student_canvas.create_window(210, 100, window=first_entry)
        new_student_canvas.create_window(370, 100, window=last_entry)
        new_student_canvas.create_window(340, 150, window=continue_button)
        new_student_canvas.create_window(240, 150, window=exit_button)

        def attempt(first, last):
            try:
                # Test input
                check_entry(first)
                check_entry(last)
            # catch for errors, create error screen if invalid entry
            except EntryException:
                error_information = tkinter.Label(text="Invalid Entry. Please check your input.", background='slate gray')
                error_button = ttk.Button(new_student_canvas, text="OK", command=lambda: (error_information.destroy(), error_button.destroy()))
                new_student_canvas.create_window(290, 300, window=error_information)
                new_student_canvas.create_window(290, 400, window=error_button)
            else:
                # Add student to database, reset screen
                create_new_student(self.database, first, last)
                new_student_canvas.destroy()
                self.create_students()

    def grading(self, assignment_num, points):
        """Grading screen for GUI"""
        # Get name and ID values, dequeue from list
        first = self.students.get_next_student().first
        last = self.students.get_next_student().last
        student_id = self.students.get_next_student().id
        self.students.dequeue()

        # Generate Canvas with labels, buttons, and input
        grading_canvas = tkinter.Canvas(self.root, width=580, height=480, background='slate gray')
        grading_canvas.pack(pady=10)
        information = tkinter.Label(text=f"Student: {first} {last} ID: {student_id}", background='slate gray')
        points_label = tkinter.Label(text=f"Points Possible: {points}", background='slate gray')
        points_entry = ttk.Entry(grading_canvas)
        next_button = ttk.Button(grading_canvas, text="Save - Next Student", command=lambda: (next_screen()))
        # If there is no next student in list, change button to main menu button
        if self.students.is_empty():
            next_button.config(text="Save - Main Menu")
        grading_canvas.create_window(290, 50, window=information)
        grading_canvas.create_window(290, 100, window=points_label)
        grading_canvas.create_window(290, 150, window=points_entry)
        grading_canvas.create_window(290, 200, window=next_button)

        def next_screen():
            # Catch errors
            try:
                set_points = int(points_entry.get())
            #  Catch errors, create error screen if invalid input
            except ValueError:
                error_information = tkinter.Label(text="Invalid Entry. Please check your input.", background='slate gray')
                error_button = ttk.Button(grading_canvas, text="OK", command=lambda: (error_information.destroy(), error_button.destroy()))
                grading_canvas.create_window(290, 300, window=error_information)
                grading_canvas.create_window(290, 400, window=error_button)
            # If valid, insert into database, reset canvas if next student, destroy and go to main menu if no next student
            else:
                insert_assignment(self.database, student_id, assignment_num, points, set_points)
                grading_canvas.destroy()
                if not self.students.is_empty():
                    self.grading(assignment_num, points)
                else:
                    self.main_menu()


if __name__ == "__main__":
    main = GradeBookGUI()
