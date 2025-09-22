# Brandon Spencer
# 09/19/2025
# P1HW2
# Coding using math/integers pt.2"

print("This program calculates and displays travel expenses")

print("Enter Budget:")

budget = float(input("Enter Budget: "))

print("Enter your travel destination: ")

destination = input("Enter your travel destination: ")

print("How much do you think you will spend on gas? ")

gas = float(input("Enter estimated gas expense: "))

print("Appoximately, how much will you need for accomodation/hotel? ")

accomodation = float(input("Enter estimated accomodation expense: "))

print("Last, how much do you need for food? ")
food = float(input("Enter estimated food expense: "))

#Come back to figure out whitespace issue, if there is a whitespace here
print("------------Travel Expenses------------")

total_expenses = gas + accomodation + food
remaining_budget = budget - total_expenses

print("Location: ", destination)
print("Initial Budget: ", budget)

print("Fuel: ", gas)
print("Accomodation: ", accomodation)
print("Food: ", food)

print("Remaining Balance: ", remaining_budget)


#Pseudocode
#Prompt user to enter budget
#Prompt user to enter travel destination

#Prompt user to enter estimated gas expense
#Prompt user to enter estimated accomodation expense
#Prompt user to enter estimated food expense

#Calculate total expenses by adding gas, accomodation, and food
#Calculate remaining budget by subtracting total expenses from initial budget

#Display travel destination, initial budget, expenses, and remaining budget