import importlib.util

spec = importlib.util.spec_from_file_location(
    "prime_number",
    "Code/06_prime_number.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

is_prime = module.is_prime


assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(7) == True
assert is_prime(10) == False
assert is_prime(1) == False
assert is_prime(0) == False
assert is_prime(-5) == False

print("All test cases passed.")