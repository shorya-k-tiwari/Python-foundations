"""
Projectile Range Calculator

Computes the horizontal range of a projectile
"""

import math

u = float(input("Enter the initial velocity (m/s): "))
theta = float(input("Enter the launch angle (degrees): "))

g = 9.81

theta_rad = math.radians(theta)

R = (u ** 2 * math.sin(2 * theta_rad)) / g

print(f"Projectile Range: {R:.2f} meters")