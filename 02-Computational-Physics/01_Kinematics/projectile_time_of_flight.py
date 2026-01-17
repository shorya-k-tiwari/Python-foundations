"""
Time of Flight Calculator

Calculates the time a projectile remains in air
"""

import math

u = float(input("Enter the velocity (u) in m/s: "))
theta = float(input("Enter angle (in degrees): "))

g = 9.8

theta_rad = math.radians(theta)

T = (2 * u * math.sin(theta_rad)) / g

print(f"Time of Flight: {T:.2f} seconds")