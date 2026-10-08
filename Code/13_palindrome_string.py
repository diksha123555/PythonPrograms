def is_palindrome_string(text):
    text = text.lower()
    return text == text[::-1]


print(is_palindrome_string("madam"))
print(is_palindrome_string("hello"))