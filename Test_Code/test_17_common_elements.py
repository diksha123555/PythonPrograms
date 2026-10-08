import importlib.util

spec = importlib.util.spec_from_file_location(
    "common_elements",
    "Code/17_common_elements.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

common_elements = module.common_elements


assert common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
assert common_elements([10, 20, 30], [20, 30, 40]) == [20, 30]
assert common_elements([1, 2, 3], [4, 5, 6]) == []
assert common_elements([1, 1, 2, 2], [1, 2]) == [1, 2]
assert common_elements([], [1, 2, 3]) == []

print("All test cases passed.")