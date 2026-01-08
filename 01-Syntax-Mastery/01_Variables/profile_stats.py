"""
Profile Statistics Calculator
Computes and displays derived study metrics for a personal profile
"""

name = "Shorya"
age = 16

daily_study_hours = 8.0
years_to_target = 1

is_disciplined = True

total_study_hours = daily_study_hours * 365 * years_to_target

print("===== Profile Statistics =====")
print(f"Name              : {name}")
print(f"Age               : {age} years")
print(f"Daily Study Hours : {daily_study_hours} hrs")
print(f"Total Study Hours : {total_study_hours:.2f} hrs")
print(f"Disciplined       : {'Yes' if is_disciplined else 'No'}")
print("==============================")