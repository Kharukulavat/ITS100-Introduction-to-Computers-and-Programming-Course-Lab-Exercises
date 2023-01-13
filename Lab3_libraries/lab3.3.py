#ITS100 Lecture3 Libraries Lab3.3
#\text{h} = \frac{\sqrt{5+2\sqrt{5}}}{2} \cdot \text{a}
from math import *
h = float(input("Enter the pentagon height: "))
a = (2*h)/sqrt(5+(2*sqrt(5)))
peri = 5*a
A = ((a**2)*sqrt(25+(10*sqrt(5))))/4
print("The length for one side of the pentagon is %.4f."%a)
print("The pentagon area and perimeter are %.4f and %.4f."%(A,peri))