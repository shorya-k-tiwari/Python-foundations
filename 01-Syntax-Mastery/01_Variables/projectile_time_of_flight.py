'''
Time of Flight: The total duration (in seconds) that a projectile 
remains in the air before hitting the target or ground.
Formula: T = (2 * u * sin(theta)) / g
'''
import math
velocity = float(input("Enter the velocity (u) in m/s:"))
theta=float(input("Enter theta (In Degrees):"))
g=9.8
radians=math.radians(theta)
T=(2*velocity*math.sin(radians))/g
print(f'Time of Flight (T) is: {T:.2f} seconds')