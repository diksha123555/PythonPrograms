def sum_of_digits(num):
    num = abs(num)
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    return total


print(sum_of_digits(1234))
print(sum_of_digits(567))