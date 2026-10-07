import os
import sys
import importlib

# Add the Code directory to the system path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))

# Load the module dynamically
module = importlib.import_module("15_second_largest")
find_second_largest = module.find_second_largest

def test_second_largest():
    assert find_second_largest([10, 20, 30, 40]) == 30
    assert find_second_largest([5, 5, 5]) == None
    assert find_second_largest([10]) == None
    assert find_second_largest([-10, -20, -5]) == -10

if __name__ == "__main__":
    test_second_largest()
    print("All test cases passed.")