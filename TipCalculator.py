print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? 10 12 15\n"))
people = int(input("How many people to split the bill?\n"))
calc = (bill + (bill*(tip/100))) / 5
print("Each person should pay:", round(calc, 2))
