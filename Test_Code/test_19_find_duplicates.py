import importlib.util

spec = importlib.util.spec_from_file_location(
    "find_duplicates", "Code/19_find_duplicates.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.find_duplicates(
    [1, 2, 2, 3, 4, 4, 5]
) == [2, 4]

assert module.find_duplicates(
    [1, 2, 3]
) == []

assert module.find_duplicates(
    [5, 5, 5, 6, 6]
) == [5, 6]

print("All test cases passed.")

