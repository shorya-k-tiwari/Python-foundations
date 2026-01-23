'''
Salary Breakdown Calculator

Computes gross salary by adding fixed allowances to basic salary
'''

basic = float(input("Enter the basic salary: "))

hra = 0.20 * basic
da  = 0.10 * basic
ta  = 0.05 * basic

gross = basic + hra + da + ta

print("\nSalary Breakdown")
print(f"Basic Salary : {basic:.2f}")
print(f"HRA (20%)    : {hra:.2f}")
print(f"DA  (10%)    : {da:.2f}")
print(f"TA  (5%)     : {ta:.2f}")
print(f"Gross Salary : {gross:.2f}")