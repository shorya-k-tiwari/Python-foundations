"""
User Information Calculator

Collects basic user data and computes simple derived metrics for display
"""

name = input("Enter your name: ")
age = int(input("Enter your age (in years): "))
height = float(input("Enter your height (in meters): "))

months = age * 12
days = age * 365
height_cm = height * 100

print(f"Type of name   : {type(name)}")
print(f"Type of age    : {type(age)}")
print(f"Type of height : {type(height)}")

print("\n--- User Information Summary ---")
print(f"Hello {name}!")
print(f"You are approximately {months} months or {days} days old")
print(f"Your height is {height} meters ({height_cm:.1f} cm)")