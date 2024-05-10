from gui import run_gui
from grading import run_tests, prepare_submission
from utils import determine_input_mode

def grade_submissions(test_cases):
    # Example: grade_submissions might interact with a filesystem or database to fetch files
    # For now, we'll simulate grading a hardcoded file
    filepath = "student_submission.py"  # Example filepath
    executable = prepare_submission(filepath)
    if executable:
        input_mode = determine_input_mode(filepath)
        results = run_tests(executable, input_mode, test_cases)
        print(f"Total tests passed: {results}/{len(test_cases)}")
    else:
        print("Failed to prepare submission.")

if __name__ == "__main__":
    run_gui(grade_submissions)
