'''
Perfect Number Checker

A perfect number is a positive integer
that equals the sum of its proper divisors
(excluding the number itself).
'''

n = int(input("Enter a number: "))

if n <= 0:
    print("Invalid input!")
    exit()

total = 0
i = 1

while i <= n // 2:
    if n % i == 0:
        total += i
    i += 1

if total == n:
    print(f"{n} is a Perfect Number")
else:
    print(f"{n} is not a Perfect Number")