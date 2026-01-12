"""
Area Calculation Menu - Version 2

Calculates the area of basic geometric shapes using functions
"""

PI = 3.14159

def show_menu():
    print("=== Area Calculation Menu ===")
    print("1. Square")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Circle")

def area_square(side):
    return side ** 2
def area_rectangle(length, width):
    return length * width
def area_triangle(base, height):
    return 0.5 * base * height
def area_circle(radius):
    return PI * radius ** 2

show_menu()
choice = input("Select a shape (1-4): ")

if choice == '1':
    shape = "Square"
    area = area_square(float(input("Enter the side length: ")))
elif choice == '2':
    shape = "Rectangle"
    area = area_rectangle(
        float(input("Enter the length: ")),
        float(input("Enter the width: "))
    )
elif choice == '3':
    shape = "Triangle"
    area = area_triangle(
        float(input("Enter the base: ")),
        float(input("Enter the height: "))
    )
elif choice == '4':
    shape = "Circle"
    area = area_circle(float(input("Enter the radius: ")))
else:
    print("Invalid choice")
    exit()

print(f"The area of the {shape} is {area}")