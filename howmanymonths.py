# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 10:03:45 2023

@author: echon
"""

import numpy as np

def compute_how_many_months(Pmt,Pv,r):
   
    # Convert the annual percentage rate (APR) to monthly interest rate
    monthly_rate = r / 100 / 12
    
    #given Pmt, Pv, r, we compute n
    
    n = - np.log( 1-Pv*monthly_rate/Pmt) / np.log(1+monthly_rate)
    n = round(n)
    return n

# Input values from the user
Pmt = float(input("Enter the monthly payment amount: "))
Pv = float(input("Enter the amount borrowed: "))
r = float(input("Enter the annual interest rate (APR): "))

# Call the function to compute the affordable loan amount
how_many_months = compute_how_many_months(Pmt,Pv,r)

# Display the result
print("# of Months:", "{:.2f}".format(how_many_months))
