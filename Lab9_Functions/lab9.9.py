#ITS100 Lecture9 Functions Lab9.9
from math import*
def myCylinder(r,h):
    v = pi*r**2*h
    a = 2*pi*r*h + 2*pi*r**2
    print("The volume is %.2f and the surface area is %.2f"%(v,a))

r = float(input("Enter the radius r of the cylinder: "))
h = float(input("Enter the height h of the cylinder: "))
myCylinder(r,h)