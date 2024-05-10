import re

def parse_binary_output(output):
    pattern = r'[01]+'
    matches = re.findall(pattern, output)
    return matches[-1] if matches else None

def determine_input_mode(filename):
    with open(filename, 'r') as file:
        contents = file.read()
    return "stdin" if "scanf" in contents or "input(" in contents else "args"

def normalize_binary(bin_str):
    return bin_str.lstrip('0') or '0'

def compare_binary_magnitude(output, expected):
    return normalize_binary(output) == normalize_binary(expected)
