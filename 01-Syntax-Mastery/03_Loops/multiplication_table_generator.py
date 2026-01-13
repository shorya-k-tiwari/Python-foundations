"""
Multiplication Table Generator

Generates a multiplication table for a given number
"""

number = int(input("Enter a number: "))
count = int(input("Enter the number of multiples to generate: "))

if count < 0:
    print("Count cannot be negative")
    exit()

print("\n=== Multiplication Table ===")

for i in range(1, count + 1):
    print(f"{number} x {i} = {number * i}")