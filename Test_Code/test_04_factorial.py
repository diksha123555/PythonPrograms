import importlib.util

spec = importlib.util.spec_from_file_location(
    "factorial",
    "Code/04_factorial.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

factorial = module.factorial


assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(3) == 6
assert factorial(5) == 120
assert factorial(7) == 5040

print("All test cases passed.")