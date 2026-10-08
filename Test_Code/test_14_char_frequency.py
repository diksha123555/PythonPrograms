import importlib.util

spec = importlib.util.spec_from_file_location(
    "char_frequency",
    "Code/14_char_frequency.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

char_frequency = module.char_frequency


assert char_frequency("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
assert char_frequency("banana") == {'b': 1, 'a': 3, 'n': 2}
assert char_frequency("abc") == {'a': 1, 'b': 1, 'c': 1}
assert char_frequency("aaa") == {'a': 3}
assert char_frequency("") == {}

print("All test cases passed.")