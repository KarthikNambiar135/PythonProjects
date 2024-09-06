import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#Taking Input
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#Initializing Password Lists and Strings
pw = []
npw = ""
#Choosing random characters/symbols/numbers
for i in range(1, nr_letters+1):
    pw.append(random.choice(letters))
for j in range(1, nr_symbols+1):
    pw.append(random.choice(symbols))
for k in range(1, nr_numbers+1):
    pw.append(random.choice(numbers))
#Shuffling the password
random.shuffle(pw)
#Convertion of List to String
for chars in pw:
    npw += chars
#Output
print("Password:")
print(npw)
