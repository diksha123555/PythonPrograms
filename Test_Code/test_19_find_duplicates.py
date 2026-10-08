import importlib.util

spec = importlib.util.spec_from_file_location(
    "find_duplicates",
    "Code/19_find_duplicates.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

find_duplicates = module.find_duplicates


assert find_duplicates([1, 2, 3, 2, 4, 1]) == [1, 2]
assert find_duplicates([10, 20, 20, 30, 30, 30]) == [20, 30]
assert find_duplicates([1, 1, 1]) == [1]
assert find_duplicates([1, 2, 3, 4]) == []
assert find_duplicates([]) == []

print("All test cases passed.")