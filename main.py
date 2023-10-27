import tkinter
from tkinter import ttk
import students.py

class GradeBookGUI:
    """Interactive grade book GUI to create assignments/grades, and run reports. """
    def __init__(self):
        # Define root and design, construct root with main_menu frame
        self.root = tkinter.Tk()
        self.root.geometry("600x500")
        self.root.configure(bg="black")
        self.main_menu()

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
        # Continue
        continue_button = ttk.Button(new_assignment_canvas, text="Continue", command=lambda: (self.root.destroy()))
        # Exit assignment creation menu, return to main menu
        exit_button = ttk.Button(new_assignment_canvas, text="Main Menu", command=lambda: (new_assignment_canvas.destroy(), self.main_menu()))
        new_assignment_canvas.create_window(290, 50, window=information)
        new_assignment_canvas.create_window(290, 100, window=assignment_entry)
        new_assignment_canvas.create_window(340, 150, window=continue_button)
        new_assignment_canvas.create_window(240, 150, window=exit_button)



if __name__ == "__main__":
    main = GradeBookGUI()
