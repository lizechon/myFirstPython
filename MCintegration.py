# -*- coding: utf-8 -*-
"""
Created on Wed Jul  23 20:50:51 2023

@author: echon
"""

def MCintegrate(f, a, b, n):
    """
    Parameters
    ----------
    f : TYPE function
    f returns a float between a and b
    a : TYPE float
    DESCRIPTION. lower limit
    b : TYPE float
    DESCRIPTION. upper limit
    n : TYPE int
    DESCRIPTION, number of random points to take in the box
    Returns
    -------
    integral of f from a to b
    """
    from random import random

    # random returns a random number between 0 and 1

    maxF = 4

    area = 0
    saveX = []
    saveY = []
    for i in range(n):

        # generate a random point in the boxc
        # x between a and b
        # z between 0 and maxF
        randNoX = random()*(b-a) + a
        randNoY = random()*maxF
        saveX.append(randNoX)
        saveX.append(randNoY)
        print(randNoX, randNoY)

        if randNoY <= f(randNoX): area += 1

    boxArea = (b-a)*maxF
    integral = area/n * boxArea
    print(min(saveX), max(saveX))
    return(integral)


if __name__ == "__main__":

    # import numpy as np
    # import matplotlib.pyplot as plt
    def f(x):
        return x**2

area = MCintegrate(f, 1., 3., 500000)

print(round(area, 2))
print(f'int {area: 0.2f}')