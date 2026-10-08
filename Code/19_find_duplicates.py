def find_duplicates(numbers):
    duplicates = []

    for num in numbers:
        if numbers.count(num) > 1 and num not in duplicates:
            duplicates.append(num)

    return duplicates


print(find_duplicates([1, 2, 3, 2, 4, 1]))
print(find_duplicates([10, 20, 20, 30, 30, 30]))