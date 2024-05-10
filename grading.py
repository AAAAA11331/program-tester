import subprocess
import os
import re
from utils import determine_input_mode, parse_binary_output, compare_binary_magnitude, normalize_binary

def prepare_submission(filename):
    extension = filename.split('.')[-1].lower()
    executable = None
    try:
        if extension == 'c':
            compile_command = f"gcc -o tempExecutable {filename} -lm"
            subprocess.run(compile_command, shell=True, check=True)
            executable = "./tempExecutable"
        elif extension == 'java':
            compile_command = f"javac {filename}"
            subprocess.run(compile_command, shell=True, check=True)
            directory = os.path.dirname(filename)
            classname = filename.split('.')[0]
            executable = f"java -classpath {directory} {classname}"
        elif extension == 'py':
            executable = f"python3 {filename}"
        else:
            raise ValueError("Unsupported file extension.")
    except subprocess.CalledProcessError:
        print(f"Compilation error in file: {filename}")
    return executable

def run_tests(executable, input_mode, test_cases):
    passed_tests = 0
    for input_args, expected_output in test_cases:
        try:
            if input_mode == "stdin":
                process = subprocess.run(executable, input=input_args.encode('utf-8'), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, timeout=10)
            else:
                full_command = f"{executable} {input_args}"
                process = subprocess.run(full_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, timeout=10)
            output = parse_binary_output(process.stdout.decode('utf-8').strip())
            if output and compare_binary_magnitude(output, expected_output):
                passed_tests += 1
                print(f"Test Case Passed: {input_args}")
            else:
                print(f"Test Case Failed: {input_args}")
        except subprocess.CalledProcessError as e:
            print(f"Error running test: {e}")
        except subprocess.TimeoutExpired:
            print("Test case timed out.")
    return passed_tests
