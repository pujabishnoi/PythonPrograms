import os
import sys
import importlib

# Add the Code directory to the system path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))

# Load the module directly from the Code directory
module = importlib.import_module("13_palindrome_string")
is_palindrome_string = module.is_palindrome_string

def test_palindrome_string():
    assert is_palindrome_string("Racecar") == True
    assert is_palindrome_string("A man, a plan, a canal: Panama") == True
    assert is_palindrome_string("hello") == False
    assert is_palindrome_string("") == True

if __name__ == "__main__":
    test_palindrome_string()
    print("All test cases passed.")