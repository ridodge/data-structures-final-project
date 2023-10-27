import tkinter
from tkinter import ttk


class GradeBookGUI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("600x500")
        self.root.configure(bg="black")
        self.main_menu()

    def main_menu(self):
        main_canvas = tkinter.Canvas(self.root, width=580, height=480, background='slate gray')
        main_canvas.pack(pady=10)
        welcome = tkinter.Label(text="Welcome to your grade book!", background='slate gray')
        main_canvas.create_window(290, 50, window=welcome)
        continue_button = ttk.Button(main_canvas, text="Continue", command=lambda: (main_canvas.destroy(), self.create_assignment()))
        main_canvas.create_window(290, 100, window=continue_button)
        return self.root.mainloop()

    def create_assignment(self):
        new_assignment_canvas = tkinter.Canvas(self.root, width=580, height=480, background='slate gray')
        new_assignment_canvas.pack(pady=10)
        information = tkinter.Label(text="Create a new assignment:", background='slate gray')
        assignment_entry = ttk.Entry(new_assignment_canvas)
        continue_button = ttk.Button(new_assignment_canvas, text="Continue", command=lambda: (self.root.destroy()))
        exit_button = ttk.Button(new_assignment_canvas, text="Main Menu", command=lambda: (new_assignment_canvas.destroy(), self.main_menu()))
        new_assignment_canvas.create_window(290, 50, window=information)
        new_assignment_canvas.create_window(290, 100, window=assignment_entry)
        new_assignment_canvas.create_window(340, 150, window=continue_button)
        new_assignment_canvas.create_window(240, 150, window=exit_button)



if __name__ == "__main__":
    main = GradeBookGUI()
