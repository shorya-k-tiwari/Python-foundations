'''
Count Digits Analyzer

Counts the number of digits in an integer using iteration
'''

n = int(input("Enter an integer: "))

def digits(value):

    if value < 0:
        value = -value

    if value == 0:
        return 1

    count = 0
    while value > 0:
        value //= 10
        count += 1

    return count

result = digits(n)
print(f"Number of digits: {result}")