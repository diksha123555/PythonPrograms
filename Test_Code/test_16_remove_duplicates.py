import importlib.util

spec = importlib.util.spec_from_file_location(
    "remove_duplicates",
    "Code/16_remove_duplicates.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

remove_duplicates = module.remove_duplicates


assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
assert remove_duplicates([10, 10, 20, 30, 30]) == [10, 20, 30]
assert remove_duplicates([1, 1, 1]) == [1]
assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
assert remove_duplicates([]) == []

print("All test cases passed.")