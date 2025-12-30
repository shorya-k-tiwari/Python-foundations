''' 
Area Calculation Menu Version 2
'''

# Constant for Pi
pi = 3.14159

# Define function to display menu
def show_menu():
    print("=== Area Calculation Menu ===")
    print("1. Square")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Circle")

# Define area calculation functions
def area_square(side):
    return side ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_circle(radius):
    return pi * radius ** 2

# Display menu
show_menu()

# Get user choice
choice = input("Select a shape (1-4): ")

# Process user choice and calculate area
if choice == '1':
    side = float(input("Enter the side length of the square: "))
    area = area_square(side)
    shape = "Square"
elif choice == '2':
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = area_rectangle(length, width)
    shape = "Rectangle" 
elif choice == '3':
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = area_triangle(base, height)
    shape = "Triangle"
elif choice == '4':
    radius = float(input("Enter the radius of the circle: "))
    area = area_circle(radius)
    shape = "Circle"
else:
    print("Invalid choice")
    exit()

# Display the result
print(f"The area of the {shape} is {area}")