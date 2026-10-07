import importlib.util

spec = importlib.util.spec_from_file_location(
    "missing_number", "Code/18_missing_number.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.missing_number([1, 2, 3, 5], 5) == 4
assert module.missing_number([1, 2, 4, 5], 5) == 3
assert module.missing_number([1, 2, 3, 4], 5) == 5

print("All test cases passed.")