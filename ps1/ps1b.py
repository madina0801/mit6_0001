# PART B. SAVING, WITH A RAISE
#User Inputs
annual_salary = float(input('Enter your annual salary: ')) #Your salary for the whole year
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: ')) #this is the percentage of what you wishes to save monthly
total_cost = float(input('Enter the cost of your dream home: '))    #total cost of the dream home
semi_annual_raise = float(input('Enter the semi annual raise, as a decimal: ')) # annual salary raise

#Variables. All amounts in (#)
current_savings = 0  #the amount that you have saved so far,starting from 0
portion_down_payment = 0.25 * total_cost
current_savings = 0  #the amount that you have saved so far,starting from 0
r = 0.04 #annual rate
annual_return = (current_savings * r) / 12
time = 0

#Iterations and Output
while (current_savings < portion_down_payment):
    monthly_salary = annual_salary / 12
    current_savings += (current_savings * r / 12) + (portion_saved * monthly_salary)  
    time += 1

    if time % 6 == 0:
        annual_salary = annual_salary + (annual_salary * semi_annual_raise)
      
print('Number of months: %d'%time)
print(annual_salary)
# In ps1b.py, copy your solution to Part A (as we are going to reuse much of that machinery).  Modify
# your program to include the following
# 1. Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage)
# 2. After the 6th month, increase your salary by that percentage.  Do the same after the 12th
# month, the 18  month, and so on. 
# Write a program to calculate how many months it will take you save up enough money for a down
# payment.  Like before, assume that your investments earn a return of r = 0.04 (or 4%) and the
# required down payment percentage is 0.25 (or 25%).  Have the user enter the following variables:
# 1. The starting annual salary (annual_salary)
# 2. The percentage of salary to be saved (portion_saved)
# 3. The cost of your dream home (total_cost)
# 4. The semi annual salary raise (semi_annual_raise)
# Hints
# To help you get started, here is a rough outline of the stages you should probably follow in writing your
# code:
# ● Retrieve user input. 
# ● Initialize some state variables. You should decide what information you need.  Be sure to be
# careful about values that represent annual amounts and those that represent monthly amounts.
# ● Be careful about when you increase your salary – this should only happen after the 6th, 12
# th, 18th month, and so on. 
# Try different inputs and see how quickly or slowly you can save enough for a down payment.  Please
# make your program print results in the format shown in the test cases below.   
# Test Case 1 
# >>>  
# Enter your starting annual salary: 120000
# Enter the percent of your salary to save, as a decimal: .05
# Enter the cost of your dream home: 500000
# Enter the semi annual raise, as a decimal: .03
# Number of months: 142 
# >>>
# Test Case 2 
# >>>  
# Enter your starting annual salary: 80000
# Enter the percent of your salary to save, as a decimal: .1
# Enter the cost of your dream home: 800000
# Enter the semi annual raise, as a decimal: .03
# Number of months: 159 
# >>>
# Test Case 3 
# >>>  
# Enter your starting annual salary: 75000
# Enter the percent of your salary to save, as a decimal: .05
# Enter the cost of your dream home: 1500000
# Enter the semi annual raise, as a decimal: .05
# Number of months: 261 