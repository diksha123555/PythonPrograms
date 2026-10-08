def missing_number(numbers):
    n = len(numbers) + 1
    total = n * (n + 1) // 2

    return total - sum(numbers)


print(missing_number([1, 2, 3, 5]))
print(missing_number([1, 2, 4, 5]))