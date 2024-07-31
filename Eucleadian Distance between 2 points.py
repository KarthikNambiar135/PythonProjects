#DISTANCE BETWEEN 2 POINTS BY USING EUCLEADIAN DISTANCE
x1 = float(input("Enter x coordinates of Point 1"))
y1 = float(input("Enter y coordinates of Point 1"))
x2 = float(input("Enter x coordinates of Point 2"))
y2 = float(input("Enter y coordinates of Point 2"))

dist = ((((x2 - x1) **2) + ((y2 - y1) **2)) * 0.5)
print("The Distance between the two given points is: ", dist, "units.")
