import importlib.util

spec = importlib.util.spec_from_file_location(
    "missing_number",
    "Code/18_missing_number.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

missing_number = module.missing_number


assert missing_number([1, 2, 3, 5]) == 4
assert missing_number([1, 2, 4, 5]) == 3
assert missing_number([1, 2, 3, 4, 6]) == 5
assert missing_number([2, 3, 4, 5]) == 1
assert missing_number([1]) == 2

print("All test cases passed.")