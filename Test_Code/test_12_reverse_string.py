import importlib.util

spec = importlib.util.spec_from_file_location(
    "reverse_string",
    "Code/12_reverse_string.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

reverse_string = module.reverse_string


assert reverse_string("Hello") == "olleH"
assert reverse_string("Python") == "nohtyP"
assert reverse_string("ABC") == "CBA"
assert reverse_string("12345") == "54321"
assert reverse_string("") == ""

print("All test cases passed.")