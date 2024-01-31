# TUAZON, FRANCESCA MARIE A. (BCS24) - S-ITCS227LA
''' 
A company SEES is in need of a payroll system that computes for the net pay of their employees. Where:
    - Gross pay = number of days worked per week times the rate per day of each employee
    - 10% of the Gross pay is being deducted as their tax
    - Rate per day is Php 347.00
    
    Display the employees Gross Pay, Deduction, and Net Pay
'''

days_worked = int(input("Enter number of days worked: "))

rate = 347.00
gross_pay = days_worked * rate
deduction = gross_pay / 10
net_pay = gross_pay - deduction

print("Gross Pay: ", gross_pay)
print("Deduction: ", deduction)
print("Net Pay: ", net_pay)
