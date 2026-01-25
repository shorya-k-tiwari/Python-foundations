"""
Triangle Type Classifier

Determines whether three given sides can form a triangle.
If valid, classifies it as Equilateral, Isosceles, or Scalene.
"""

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a <= 0 or b <= 0 or c <= 0:
    result = "Invalid input: sides must be positive"

elif a + b <= c or a + c <= b or b + c <= a:
    result = "Not a triangle"

elif a == b == c:
    result = "Equilateral triangle"

elif a == b or b == c or a == c:
    result = "Isosceles triangle"

else:
    result = "Scalene triangle"

print(f"Result: {result}")