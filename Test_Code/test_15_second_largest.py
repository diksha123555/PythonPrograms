import importlib.util

spec = importlib.util.spec_from_file_location(
    "second_largest",
    "Code/15_second_largest.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

second_largest = module.second_largest


assert second_largest([10, 20, 30, 40]) == 30
assert second_largest([5, 15, 25, 35]) == 25
assert second_largest([10, 50, 20, 40]) == 40
assert second_largest([1, 2, 3]) == 2
assert second_largest([5, 5, 3, 2]) == 3

print("All test cases passed.")