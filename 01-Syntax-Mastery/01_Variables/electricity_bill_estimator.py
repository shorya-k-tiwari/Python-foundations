# Electricity Bill Estimator

units = float(input('Enter the number of electricity units consumed:'))
if units <= 100:
    cost = units * 2.0
    print('Total Electricity Bill is:', cost)
elif units <= 300:
    cost = units * 3.0
    print('Total Electricity Bill is:', cost)
else:
    cost = units * 5.0
    print('Total Electricity Bill is:', cost)
