'''
Temperature 

This program converts a temperature value between
Celsius and Fahrenheit based on user input

Accepted units:
C → Celsius
F → Fahrenheit
'''

value = float(input('Enter temperature value: '))

unit = input('Enter unit (C for Celsius, F for Fahrenheit): ').strip().upper()

if unit == 'C':
    converted = (value * 9 / 5) + 32
    target_unit = 'F'

elif unit == 'F':
    converted = (value - 32) * 5 / 9
    target_unit = 'C'

else:
    print('Invalid unit entered!')
    exit()

print(f'Converted temperature: {converted:.2f} {target_unit}')