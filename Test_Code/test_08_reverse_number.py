import importlib.util

spec = importlib.util.spec_from_file_location(
    "reverse_number",
    "Code/08_reverse_number.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

reverse_number = module.reverse_number


assert reverse_number(1234) == 4321
assert reverse_number(567) == 765
assert reverse_number(100) == 1
assert reverse_number(12321) == 12321
assert reverse_number(0) == 0
assert reverse_number(-123) == -321

print("All test cases passed.")