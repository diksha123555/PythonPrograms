import importlib.util

spec = importlib.util.spec_from_file_location(
    "palindrome_string",
    "Code/13_palindrome_string.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

is_palindrome_string = module.is_palindrome_string


assert is_palindrome_string("madam") == True
assert is_palindrome_string("hello") == False
assert is_palindrome_string("level") == True
assert is_palindrome_string("Python") == False
assert is_palindrome_string("racecar") == True
assert is_palindrome_string("") == True

print("All test cases passed.")
