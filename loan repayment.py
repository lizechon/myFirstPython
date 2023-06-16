# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 21:02:02 2023

@author: echon
"""

def PMT(PV, r, n):
    # Repayment formula
    loan_payment = r * PV/(1-(1+r)**-n)
    
    return loan_payment

# Inputs
PV = float(input("Enter the Present Value:$"))      # Present Value
r = float(input("Enter interest rate %: "))         # APR 
n = int(input("Enter the number of Months:"))       # Months  

r = r/100/12   
loan_payment = PMT(PV, r, n)

print("$", round(loan_payment))
