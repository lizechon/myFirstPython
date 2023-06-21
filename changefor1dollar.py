# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 17:34:48 2023

@author: lechon
"""
def make_change(amount):
    denominations = [1, 5, 10, 25, 50]
    ways = [0] * (amount + 1)
    ways[0] = 1

    for coin in denominations:
        for i in range(coin, amount + 1):
            ways[i] += ways[i - coin]

    return ways[amount]

total_ways = make_change(100)  # Calculate the total ways for $1
print("Total number of ways to make change for $1:", total_ways)
