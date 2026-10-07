# Test_Code/test20_word_frequency.py
import importlib.util

spec = importlib.util.spec_from_file_location("word_frequency", "Code/20_word_frequency.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.count_word_frequency("hello world hello") == {"hello": 2, "world": 1}
assert module.count_word_frequency("Apple banana apple") == {"apple": 2, "banana": 1}
assert module.count_word_frequency("") == {}

print("All test cases passed.")