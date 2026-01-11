"""
Temperature Classifier

Classifies a temperature value into defined ranges
"""

temperature = float(input("Enter temperature in Celsius: "))

if temperature >= 40:
    classification = "Very Hot"
elif temperature >= 30:
    classification = "Hot"
elif temperature >= 20:
    classification = "Warm"
elif temperature >= 10:
    classification = "Cool"
else:
    classification = "Cold"

print(f"Temperature Classification: {classification}")