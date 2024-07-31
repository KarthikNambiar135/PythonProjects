#AVERAGE OF 2 NUMBERS AND THEIR DEVIATION
a = float(input("Enter First Number"))
b = float(input("Enter Second Number"))
avg = int((a+b)/2)
print("Average of given two numbers is: ", avg)
dev = a - avg
dev1 = b - avg
print("Deviation of First Number is: ", dev)
print("Deviation of Second Number is: ", dev1)
