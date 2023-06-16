# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 00:13:12 2023

@author: echon
"""
#### chatGPT prompt "Write a python program to compute loan monthly repayment amount: 
### Present Value (PV) = 12000, r = 7.45 (APR), n = 48 months, Use the formula 
## Pmt = r * PV/(1-(1+r)**-n), and create a function that takes PV, r and n as variable 
# inputs by the user and final output should only have 2 decimal places"

def compute_monthly_repayment(PV, r, n):
    # Convert the annual percentage rate (APR) to monthly interest rate
    monthly_rate = r / 100 / 12

    # Compute the monthly repayment amount using the provided formula
    Pmt = monthly_rate * PV / (1 - (1 + monthly_rate) ** -n)
    return Pmt

# Input values from the user
PV = float(input("Enter the Present Value (PV): "))
r = float(input("Enter the annual interest rate (APR): "))
n = int(input("Enter the number of months (n): "))

# Call the function to compute the monthly repayment amount
monthly_repayment = compute_monthly_repayment(PV, r, n)

# Format the result to display with two decimal places
formatted_repayment = "{:.2f}".format(monthly_repayment)

# Display the result
print("Monthly Repayment Amount:", formatted_repayment)
