from grading import *
from gui import *
from utils import *

def grade_submissions(test_cases):
    filename = "./test/hi.py"  # Replace with the actual filename
    executable = prepare_submission(filename)
    input_mode = determine_input_mode(filename)
    results = run_tests(executable, input_mode, test_cases)
    return results

if __name__ == "__main__":
    run_gui()
