"""
Greatest of Three Numbers

Determines the maximum value among three integers
using direct conditional comparisons
"""

a = int(input('Enter First Number: '))
b = int(input('Enter Second Number: '))
c = int(input('Enter Third Number: '))

if a == b == c:
    greatest = a
elif a >= b and a >= c:
    greatest = a
elif b >= a and b >= c:
    greatest = b
else:
    greatest = c

print(f'Greatest Number: {greatest}')