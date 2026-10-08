import importlib.util

spec = importlib.util.spec_from_file_location(
    "word_frequency",
    "Code/20_word_frequency.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

word_frequency = module.word_frequency


assert word_frequency("hello world hello") == {
    "hello": 2,
    "world": 1
}

assert word_frequency("python is easy python is fun") == {
    "python": 2,
    "is": 2,
    "easy": 1,
    "fun": 1
}

assert word_frequency("apple apple apple") == {
    "apple": 3
}

assert word_frequency("one two three") == {
    "one": 1,
    "two": 1,
    "three": 1
}

assert word_frequency("") == {}

print("All test cases passed.")