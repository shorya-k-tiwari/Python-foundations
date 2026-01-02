'''
Armstrong Number Checker
'''

# Take integer input from the user
n = int(input('Enter a Number: '))

# Variable to store the sum of powered digits
total = 0

# Negative numbers cannot be Armstrong numbers
if n < 0:
    answer = 'Not an Armstrong Number'

# Zero is considered an Armstrong number
elif n == 0:
    answer = 'Armstrong Number'

else:
    
    # Count the number of digits in the number
    count = 0
    temp = n
    while temp != 0:
        count += 1
        temp //= 10
    
    # Calculate the Armstrong sum using the digit count
    original = n
    while original != 0:
        digit = original % 10
        total = total + digit ** count
        original //= 10 
    
    # Compare calculated sum with the original number
    if n == total:
        answer = 'Armstrong Number'
    else:
        answer = 'Not an Armstrong Number'

# Display the result
print(f'{n} ---> {answer}')