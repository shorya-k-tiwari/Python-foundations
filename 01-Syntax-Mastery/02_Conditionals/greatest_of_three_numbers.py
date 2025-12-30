'''
Greatest of Three Numbers
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