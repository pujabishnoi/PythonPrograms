import os
import sys
import importlib

# Add the Code directory to the system path to prevent import errors
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))

# Load the module dynamically
module = importlib.import_module("16_remove_duplicates")
remove_duplicates = module.remove_duplicates

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates(["a", "b", "a", "c"]) == ["a", "b", "c"]
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 1, 1]) == [1]

if __name__ == "__main__":
    test_remove_duplicates()
    print("All test cases passed.")