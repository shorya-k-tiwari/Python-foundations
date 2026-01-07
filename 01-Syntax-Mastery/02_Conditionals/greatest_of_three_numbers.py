'''
Greatest of Three Numbers

Greatest of Three Numbers is the maximum value among three given numbers, 
identified through direct comparisons like if A ≥ B and A ≥ C
'''

# Get inputs
a = int(input('Enter First Number: '))
b = int(input('Enter Second Number: '))
c = int(input('Enter Third Number: '))

# Check if all are equal
if a == b == c:
    print('All numbers are equal')

# Determine the greatest number
elif a >= b and a >= c:
    n = a
elif b >= a and b >= c:
    n = b
else:
    n = c

# Printing Result
print(f'Greatest Number: {n}')