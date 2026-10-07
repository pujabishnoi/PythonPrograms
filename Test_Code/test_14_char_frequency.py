import os
import sys
import importlib

# Add the Code directory to the system path to prevent errors
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))

# Load the module dynamically
module = importlib.import_module("14_char_frequency")
count_char_frequency = module.count_char_frequency

def test_char_frequency():
    assert count_char_frequency("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    assert count_char_frequency("aba") == {'a': 2, 'b': 1}
    assert count_char_frequency("") == {}

if __name__ == "__main__":
    test_char_frequency()
    print("All test cases passed.")