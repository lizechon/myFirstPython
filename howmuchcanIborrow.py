# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 10:03:45 2023

@author: echon
"""
# Used chatGPT to clean up code 

def compute_monthly_repayment(PV, r, n):
    # Convert the annual percentage rate (APR) to monthly interest rate
    monthly_rate = r / 100 / 12

    # Compute the monthly repayment amount using the provided formula
    Pmt = monthly_rate * PV / (1 - (1 + monthly_rate) ** -n)
    return Pmt

def compute_affordable_loan_amount(Pmt, r, n):
    # Convert the annual percentage rate (APR) to monthly interest rate
    monthly_rate = r / 100 / 12

    # Compute the affordable loan amount using the provided formula
    Pv = (1 - (1 + monthly_rate) ** -n) * Pmt / monthly_rate
    return Pv

# Input values from the user
Pmt = float(input("Enter the monthly payment amount: "))
r = float(input("Enter the annual interest rate (APR): "))
n = int(input("Enter the number of months (n): "))

# Call the function to compute the affordable loan amount
affordable_loan_amount = compute_affordable_loan_amount(Pmt, r, n)

# Display the result
print("Affordable Loan Amount:", "{:.2f}".format(affordable_loan_amount))
