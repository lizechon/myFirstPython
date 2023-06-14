# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# chatGPT generated code

def compute_height(initial_velocity, time):
    # Constants
    gravity = 9.8  # Acceleration due to gravity (m/s^2)

    # Calculate height
    height = (initial_velocity * time) - (0.5 * gravity * time ** 2)

    return height

# Input values
initial_velocity = 5.0  # Initial velocity in m/s
time = 0.6  # Time in seconds

# Compute the height
ball_height = compute_height(initial_velocity, time)

# Print the result
print("The height of the ball is:", ball_height, "m")

# Program for computing the height of a ball in vertical motion (found in book)

v0 = 5      # Initial velocity
g = 9.81    # Acceleration of gravity
t = 0.6     # Time

y = v0*t - 0.5*g*t**2 # Vertical position
print(y,'m')