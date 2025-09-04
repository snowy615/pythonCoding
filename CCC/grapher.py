import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import *

data = pd.read_csv('1-1v.csv')

time = data['Time']
traj = data['Traj']

def get_y(m, b, x):
    return acos(np.clip(m * x * x + b, -1, 1))*180/pi

def calculate_error(m, b, point):
    x_point = point[0]
    y_point = point[1]
    error = abs(y_point - get_y(m, b, x_point))
    return error

def calculate_all_error(m, b, points):
    total_error = 0
    for point in points:
        total_error += calculate_error(m, b, point)
    return total_error

datapoints = [(velocity[i], theta[i]) for i in range(len(velocity))]

possible_ms = [i / 1000000 for i in range(-8000, -7500)]
possible_bs = [i / 100 for i in range(-200, 201)]

smallest_error = float('inf')
best_m = 0
best_b = 1

for m in possible_ms:
    # for b in possible_bs:
    error = calculate_all_error(m, 1, datapoints)
    if error < smallest_error:
        best_m = m
        best_b = 1
        smallest_error = error

print(f"Best m: {best_m}")
print(f"Best b: {best_b}")

print(f"Predicted theta for velocity=3.1: {get_y(best_m, best_b, 3.1)}")

x_fit = np.linspace(0, 16, 100)
y_fit = [get_y(best_m, best_b, x) for x in x_fit]



# -----------------------------------UNCERTAINTY: ONLY CHANGE THE FOLLOWING VALUES-------------------------------------#

velocity_uncertainty = 0.7
theta_uncertainty = 8
print(theta_uncertainty)





# PLOTTING!!! DO NOT CHANGE!!!!
plt.figure(figsize=(10, 6))
plt.errorbar(velocity, theta, xerr=velocity_uncertainty, yerr=theta_uncertainty, fmt='o', label='Uncertainty Bars', color='red', ecolor='black', elinewidth=1, capsize=3)
plt.plot(x_fit, y_fit, label=f'y = cos⁻¹({best_m}x² + {best_b})', color='blue')
plt.xlabel('Velocity of the Projectile (v / ms⁻¹)')
plt.ylabel('Maximum Angular Displacement of the Pendulum (θ / °)')
plt.legend()
plt.title('Maximum Angular Displacement of the Pendulum VS Velocity of the Projectile')
plt.grid(True)
plt.show()
