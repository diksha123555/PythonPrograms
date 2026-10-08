import importlib.util

spec = importlib.util.spec_from_file_location(
    "pos_neg_zero",
    "Code/03_pos_neg_zero.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

check_number = module.check_number


assert check_number(10) == "Positive"
assert check_number(5) == "Positive"
assert check_number(-5) == "Negative"
assert check_number(-10) == "Negative"
assert check_number(0) == "Zero"

print("All test cases passed.")