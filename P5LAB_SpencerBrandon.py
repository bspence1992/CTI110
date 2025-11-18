# Brandon Spencer
# 11-18-25
# P5LAB
# Simulating a customer using self-checkout machine, machine displays back the amount in into dollars, quarters, dimes, nickels and pennies

import random
amount_owed = round(random.uniform(0.01, 100.00), 2)

# You owe:
print(f"You owe: ${amount_owed:.2f}")

# How much cash will you put in the self-checkout?
def main():
	try:
		amount_float = float(input("How much cash will you put in the self-checkout?: $"))
	except ValueError:
		print("Invalid amount.")
		return

	if amount_float == 0:
		print("No change.")
		return

# Change owed is:
	amount_float -= amount_owed
	print(f"Change is: ${amount_float:.2f}")

	# STEP 1: Convert to pennies (use round to avoid floating point issues)
	amount = int(round(amount_float * 100))
	# STEP 2, Remove all the dollars
	dollars = amount // 100 # "//" <-- means integer Division
	amount = amount % 100 # "%" <-- means keep the REMAINDER
	# do the rest of the math (25, 10, 5, and 1)
	quarters = amount // 25
	amount = amount % 25
	dimes = amount // 10
	amount = amount % 10
	nickels = amount // 5
	amount = amount % 5
	pennies = amount
	# LAST STEP: Print the answer
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

if __name__ == "__main__":
	main()
