# Brandon Spencer
# P3LAB
# 10-9-25
# Get amount of money, break into change

# FIRST, find out how many dollars.
amount_float = float(input("Enter a dollar amount with decimals: $"))

if (amount_float == 0):
    print("No change.")

# STEP 1: Convert to pennies
amount = int(amount_float * 100)
print("That is", amount, "pennies.")

# STEP 2, Remove all the dollars
dollars = amount // 100  # "//" <-- means integer Division
amount = amount % 100    # "%"  <-- means keep the REMAINDER

# TODO: do the rest of the math (25, 10, 5, and 1)
quarters = amount // 25
amount = amount % 25

dimes = amount // 10
amount = amount % 10

nickels = amount // 5

pennies = amount # fix this

# LAST STEP: Print the answer
# Print (dollars, "dollars, and ", amount, "pennies")
if dollars > 0:
    print(dollars, "Dollars")
if quarters > 0:
    print(quarters, "Quarters")
if dimes > 0:
    print(dimes, "Dimes")
if nickels > 0:
    print(nickels, "Nickels")
if pennies > 0:
    print(pennies, "Pennies")