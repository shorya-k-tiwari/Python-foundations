'''
Leap Year Checker

Determines whether a given year is a leap year
using standard calendar rules
'''

year = int(input("Enter a year: "))

leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

result = "Leap Year" if leap else "Not a Leap Year"

print(result)