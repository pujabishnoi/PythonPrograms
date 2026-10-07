import importlib.util

spec = importlib.util.spec_from_file_location(
    "largest", "Code/02_largest_of_three.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.largest_of_three(10, 20, 30) == 30
assert module.largest_of_three(50, 20, 30) == 50
assert module.largest_of_three(10, 60, 30) == 60
assert module.largest_of_three(5, 5, 5) == 5

print("All test cases passed.")