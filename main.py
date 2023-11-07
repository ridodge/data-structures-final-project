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

        self.create_students()
        self.root.mainloop()



    def main_menu(self):
        """Main menu of grade book"""
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
        return self.root.mainloop()

    def create_assignment(self):
        """Create assignment menu of grade book"""
        # Define create assignment menu
        new_assignment_canvas = tkinter.Canvas(self.root, width=580, height=480, background='slate gray')
        new_assignment_canvas.pack(pady=10)
        # Informative label to guide user
        information = tkinter.Label(text="Create a new assignment:", background='slate gray')
        # Entry point for assignment name
        assignment_entry = ttk.Entry(new_assignment_canvas)
        # Continue button
        continue_button = ttk.Button(new_assignment_canvas, text="Continue", command=lambda: (self.root.destroy()))
        # Exit assignment creation menu, return to main menu
        exit_button = ttk.Button(new_assignment_canvas, text="Main Menu", command=lambda: (new_assignment_canvas.destroy(), self.main_menu()))
        new_assignment_canvas.create_window(290, 50, window=information)
        new_assignment_canvas.create_window(290, 100, window=assignment_entry)
        new_assignment_canvas.create_window(340, 150, window=continue_button)
        new_assignment_canvas.create_window(240, 150, window=exit_button)

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
        continue_button = ttk.Button(new_student_canvas, text="Next Student", command=lambda: (attempt(self.database, first_entry.get(), last_entry.get())))
        # Exit student creation menu, return to main menu
        exit_button = ttk.Button(new_student_canvas, text="Done", command=lambda: (new_student_canvas.destroy(), self.main_menu()))
        new_student_canvas.create_window(290, 50, window=information)
        new_student_canvas.create_window(210, 75, window=fname)
        new_student_canvas.create_window(370, 75, window=lname)
        new_student_canvas.create_window(210, 100, window=first_entry)
        new_student_canvas.create_window(370, 100, window=last_entry)
        new_student_canvas.create_window(340, 150, window=continue_button)
        new_student_canvas.create_window(240, 150, window=exit_button)

        def attempt(database, first, last):
            try:
                test_entry(first)
                test_entry(last)
            except EntryException:
                error_information = tkinter.Label(text="Invalid Entry. Please check your input.", background='slate gray')
                error_button = ttk.Button(new_student_canvas, text="OK", command=lambda: (error_information.destroy(), error_button.destroy()))
                new_student_canvas.create_window(290, 300, window=error_information)
                new_student_canvas.create_window(290, 400, window=error_button)
            else:
                create_new_student(database, first, last)
                new_student_canvas.destroy()
                self.create_students()


if __name__ == "__main__":
    main = GradeBookGUI()
