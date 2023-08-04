# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:46:39 2023

@author: echon
"""

import numpy as np
import matplotlib.pyplot as plt


A = np.array([[2, -1, 3],
              [-1, 3, -1],
              [4, -4, 3]])


b = np.array([10, -1, 3])


x = np.linalg.solve(A, b)

print("Solution:")
print("x1 =", x[0])
print("x2 =", x[1])
print("x3 =", x[2])


x_vals = np.linspace(-5, 5, 100)
eq1 = (10 - 2 * x_vals + 3 * x_vals**2) / x_vals
eq2 = (-1 + x_vals + x_vals**2) / 3
eq3 = (3 + 4 * x_vals - 4 * x_vals**2) / 3

plt.figure(figsize=(8, 6))
plt.plot(x_vals, eq1, label='2*x1 - x2 + 3*x3 = 10')
plt.plot(x_vals, eq2, label='-x1 + 3*x2 - x3 = -1')
plt.plot(x_vals, eq3, label='4*x1 - 4*x2 + 3*x3 = 3')
plt.xlabel('x1')
plt.ylabel('x2 and x3')
plt.title('System of Equations')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
plt.grid(True)
plt.show()