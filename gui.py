import tkinter as tk
from tkinter import messagebox, filedialog
from main import grade_submissions
import os


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.filename = None
        self.directory = None

    def create_widgets(self):
        self.upload_file_button = tk.Button(self, text="Upload File", command=self.upload_file)
        self.upload_file_button.pack()

        self.upload_directory_button = tk.Button(self, text="Upload Directory", command=self.upload_directory)
        self.upload_directory_button.pack()

        self.test_input_label = tk.Label(self, text="Test Input")
        self.test_input_label.pack()
        self.test_input_entry = tk.Entry(self)
        self.test_input_entry.pack()

        self.test_output_label = tk.Label(self, text="Expected Output")
        self.test_output_label.pack()
        self.test_output_entry = tk.Entry(self)
        self.test_output_entry.pack()

        self.add_button = tk.Button(self, text="Add Test Case", command=self.add_test_case)
        self.add_button.pack()

        self.test_cases_listbox = tk.Listbox(self)
        self.test_cases_listbox.pack()

        self.grade_button = tk.Button(self, text="Run Grading", command=self.run_grading)
        self.grade_button.pack()

        self.clear_button = tk.Button(self, text="Clear Results", command=self.clear_results)
        self.clear_button.pack()

        self.results_text = tk.Text(self, height=10, width=50)
        self.results_text.pack()

    def upload_file(self):
        self.filename = filedialog.askopenfilename()
        if self.filename:
            messagebox.showinfo("File Selected", f"Selected file: {self.filename}")
            self.directory = None  # Reset directory selection if a file is selected

    def upload_directory(self):
        self.directory = filedialog.askdirectory()
        if self.directory:
            messagebox.showinfo("Directory Selected", f"Selected directory: {self.directory}")
            self.filename = None  # Reset file selection if a directory is selected

    def add_test_case(self):
        test_input = self.test_input_entry.get()
        test_output = self.test_output_entry.get()
        if test_input and test_output:
            test_case = f"{test_input};{test_output}"
            self.test_cases_listbox.insert(tk.END, test_case)
            self.test_input_entry.delete(0, tk.END)
            self.test_output_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Both test input and expected output must be provided")

    def run_grading(self):
        raw_test_cases = self.test_cases_listbox.get(0, tk.END)
        try:
            test_cases = [tuple(tc.split(";")) for tc in raw_test_cases if ";" in tc]
            if len(test_cases) != len(raw_test_cases):
                raise ValueError("Some test cases are not correctly formatted (input;expected_output).")

            if self.filename:
                results = grade_submissions(test_cases, self.filename)
                self.results_text.insert(tk.END, f"File: {self.filename}\n")
                self.results_text.insert(tk.END, f"Passed {results} out of {len(test_cases)} test cases.\n")
            elif self.directory:
                for file in os.listdir(self.directory):
                    if file.endswith(('.py', '.java', '.c')):
                        filepath = os.path.join(self.directory, file)
                        results = grade_submissions(test_cases, filepath)
                        self.results_text.insert(tk.END, f"File: {filepath}\n")
                        self.results_text.insert(tk.END, f"Passed {results} out of {len(test_cases)} test cases.\n")
            else:
                messagebox.showerror("Error", "No file or directory selected")

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))

    def clear_results(self):
        self.results_text.delete('1.0', tk.END)


def run_gui():
    root = tk.Tk()
    app = Application(master=root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()
