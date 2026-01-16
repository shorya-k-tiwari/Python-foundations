"""
Parity and Sign Analyzer

Analyzes a set of integers for sign and parity
"""

odd = even = positive = negative = zero = 0

count = int(input("Enter how many numbers you will enter: "))

if count < 0:
    print("Count cannot be negative")
    exit()

for _ in range(count):
    n = int(input("Enter a number: "))

    if n > 0:
        positive += 1
    elif n < 0:
        negative += 1
    else:
        zero += 1

    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("\n=== Summary ===")
print(f"Positive Numbers : {positive}")
print(f"Negative Numbers : {negative}")
print(f"Zeroes           : {zero}")
print(f"Odd Numbers      : {odd}")
print(f"Even Numbers     : {even}")