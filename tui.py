import tkinter as tk
from tkinter import messagebox

class GradingApp:
    def __init__(self, master, grade_callback):
        self.master = master
        master.title("Grading Tool")

        self.test_case_entry = tk.Entry(master)
        self.test_case_entry.pack()

        self.add_button = tk.Button(master, text="Add Test Case", command=self.add_test_case)
        self.add_button.pack()

        self.test_cases_listbox = tk.Listbox(master)
        self.test_cases_listbox.pack()

        self.grade_button = tk.Button(master, text="Run Grading", command=lambda: grade_callback(self.test_cases_listbox.get(0, tk.END)))
        self.grade_button.pack()

        self.results_text = tk.Text(master, height=10, width=50)
        self.results_text.pack()

        self.test_cases = []

    def add_test_case(self):
        test_case = self.test_case_entry.get()
        if test_case:
            self.test_cases.append(test_case)
            self.test_cases_listbox.insert(tk.END, test_case)
            self.test_case_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Test case cannot be empty")

def run_gui(grade_callback):
    root = tk.Tk()
    app = GradingApp(root, grade_callback)
    root.mainloop()
