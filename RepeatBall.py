# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 18:39:57 2023

@author: lechon
"""
### Question asked "Write a Python program that takes inputs from the 
##console: v0 the initial velocity of the ball ft/sec (thrown upward), 
#force of gravity (g = 32.8 ft/sec/sec), and compute the maximum height the ball reaches"

def calculate_max_height(v0, g):
    max_height = (v0 ** 2) / (2 * g)  # Formula to calculate maximum height
    return max_height

# Getting inputs from the user
v0 = float(input("Enter the initial velocity of the ball (ft/sec): "))
g = 32.8  # Acceleration due to gravity (ft/sec/sec)

# Calculating the maximum height
max_height = calculate_max_height(v0, g)

# Displaying the result
print("The maximum height reached by the ball is:", max_height, "ft")



# To add time as an input asked chatGPT "with an input of time as well" 

def calculate_height(v0, g, t):
    height = v0 * t - 0.5 * g * (t ** 2)  # Formula to calculate height at time t
    return height

# Getting inputs from the user
v0 = float(input("Enter the initial velocity of the ball (ft/sec): "))
g = 32.8  # Acceleration due to gravity (ft/sec/sec)
t = float(input("Enter the time (sec): "))

# Calculating the height at time t
height = calculate_height(v0, g, t)

# Displaying the result
print("The height of the ball at time", t, "seconds is:", height, "ft")