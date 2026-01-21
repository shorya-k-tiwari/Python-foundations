'''
Strong Number Checker

A strong number is a number whose sum of the factorial
of its digits equals the number itself
'''

n = int(input("Enter a number: "))
original = n
total = 0

while n > 0:
    digit = n % 10

    factorial = 1
    i = 2
    while i <= digit:
        factorial *= i
        i += 1

    total += factorial
    n //= 10

if total == original:
    print(f"{original} is a Strong Number")
else:
    print(f"{original} is not a Strong Number")