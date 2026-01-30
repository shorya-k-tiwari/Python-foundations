'''
Count Digits Analyzer

Counts the number of digits in an integer using iteration
'''

n = int(input("Enter an integer: "))

value = n
if value < 0:
    value = -value

if value == 0:
    count = 1
else:
    count = 0
    while value > 0:
        value //= 10
        count += 1

print(f"Number of digits: {count}")