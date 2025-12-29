''' 
Area Calculation Menu Version 2
'''


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
    return 3.14159 * radius ** 2

if __name__ == "__main__":