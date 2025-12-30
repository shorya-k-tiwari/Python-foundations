'''
Factorial Calculator
'''

# Get user input
n = int(input("Enter a non-negative integer: "))

# Calculate factorial using iterative approach
if n > 0:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i 
elif n == 0:
    factorial = 1
else: 
    print("Factorial is not defined for negative numbers")
    exit()

# Display the result
print(f"The factorial of {n}! is: {factorial}")