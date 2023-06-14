# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 17:21:57 2023

@author: lechon
"""

# Program for computing the height of a ball in vertical motion (found in book) calculated in ft

v0 = 5      # Initial velocity
g = 32.8    # Acceleration of gravity in ft/sec/sec
t = 0.6     # Time

y = v0*t - 0.5*g*t**2 # Vertical position
print(y,'ft')
