"""
Type Inspector
Collects user input, converts values to basic data types, and displays their types
"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
student_response = input("Are you a student? (yes/no): ").strip().lower()

is_student = student_response == "yes"

print('\n', '|======== Output ========|')
print(f"Name    : {name} | Type -> {type(name)}")
print(f"Age     : {age} | Type -> {type(age)}")
print(f"Height  : {height} | Type -> {type(height)}")
print(f"Student : {is_student} | Type -> {type(is_student)}")