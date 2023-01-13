#ITS100 Lecture9 Functions Lab9.10
from math import*
def SquareArea(x):
    sarea = l**2
    print("")
    print("The area of the square is %.2f"%sarea)

def CircleArea(r):
    carea = pi*r**2
    print("")
    print("The area of the circle is %.2f"%carea)
    
    
find = input("Do you want to find the area of a square (s) or a circle (c)?: ")
if find == "s" or find == "c":
    if find == "s":
        l = float(input("Enter the lenght: "))
        SquareArea(l)
    elif find == "c":
        r = float(input("Enter the radius: "))
        CircleArea(r)
else:
    print("")
    print("Wrong Input")
