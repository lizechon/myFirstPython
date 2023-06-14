# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 17:34:48 2023

@author: lechon
"""

def height(v0, t):
    # Constants
    g = 32.8  # Acceleration due to gravity (ft/s^2)

    # Calculate height
    y = (v0 * t) - (0.5 * g * t ** 2)

    return y
t=1
while t > 0:
    v0 = input('input velocity, ft: ')
    v0 = float(v0)
    t = input('input time, sec: ')
    t = float(t)
    y = height(v0, t)

    print(f'after {t} seconds height = {y} ft')    
    
"""
At time 1.6 ball got to its max height which was about 38 feet. Assuming we throw it vertically at initial velocity of 50 ft.
"""
