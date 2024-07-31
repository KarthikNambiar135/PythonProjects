#AREA OF TRIANGLE USING HERON'S FORMULA
a = float(input("Enter the Length of Side 1"))
b = float(input("Enter the Lenght of Side 2"))
c = float(input("Enter the Lenght of Side 3"))
s = (a + b + c)/2
area = ((s * (s-a) * (s-b) * (s-c)) * 0.5)
print("Area of Triangle with the given dimesnions is: ", area, "units.")
