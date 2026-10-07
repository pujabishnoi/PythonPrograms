import sys
import os
import importlib

# Add the project root directory to Python's path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Dynamically load the module to bypass number syntax issues
string_module = importlib.import_module("Code.12_reverse_string")
reverse_string = string_module.reverse_string

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""
    assert reverse_string("racecar") == "racecar"

if __name__ == "__main__":
    test_reverse_string()
    print("All test cases passed.")