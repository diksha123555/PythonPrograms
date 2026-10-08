import importlib.util

spec = importlib.util.spec_from_file_location(
    "vowels_consonants",
    "Code/11_vowels_consonants.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

check_vowels_consonants = module.check_vowels_consonants


assert check_vowels_consonants("Hello") == (2, 3)
assert check_vowels_consonants("Python") == (1, 5)
assert check_vowels_consonants("Apple") == (2, 3)
assert check_vowels_consonants("AEIOU") == (5, 0)
assert check_vowels_consonants("123") == (0, 0)

print("All test cases passed.")