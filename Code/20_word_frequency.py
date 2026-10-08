def word_frequency(text):
    frequency = {}

    words = text.lower().split()

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


print(word_frequency("hello world hello"))
print(word_frequency("python is easy python is fun"))