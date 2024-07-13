## Author: Francisco Bumanglag
## Project: TIP TAX TOTAL
## Assignment: Module 1 Project 3
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: June 18, 2023


#INPUT INFORMATION
mealCost = float(input('Enter the amount of the meal purchase: $'))

#CALCUATIONS
tipPercent = .18 
salesPercent = .07

tipAmount = mealCost * tipPercent
salesAmt = mealCost * salesPercent

totalMeal = mealCost + tipAmount +  salesAmt

#OUTPUT 
print('The tip amount is: ${:.2f}'.format(tipAmount))
print('The sales amount is: ${:.2f}'.format(salesAmt))
print('The total cost of your meal is: ${:.2f}'.format(totalMeal))





