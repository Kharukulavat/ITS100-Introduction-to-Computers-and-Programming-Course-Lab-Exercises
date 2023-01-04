#ITS100 Lecture2 Variables, Input and Output Lab 2.3
r = input("Input Radius (cm) = ")
h = input("Input Height (cm) = ")
r,h = float(r),float(h)
Pi = 3.1415926535
V = Pi*(r**2)*h
print("The volume of cylinder is %.5f cubic centimeter."%V)