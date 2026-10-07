import sys
import os
import importlib

# Ensures Python can locate the root directory properly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Dynamically loads the module to bypass number syntax errors
vowels_module = importlib.import_module("Code.11_vowels_consonants")
count_vowels_consonants = vowels_module.count_vowels_consonants

def test_vowels_consonants():
    assert count_vowels_consonants("Hello") == (2, 3)
    assert count_vowels_consonants("Python") == (1, 5)
    assert count_vowels_consonants("123!!!") == (0, 0)
    assert count_vowels_consonants("") == (0, 0)

if __name__ == "__main__":
    test_vowels_consonants()
    print("All test cases passed.")