#ITS100 Lecture3 Libraries Lab3.4
from math import *
x1 = float(input("Enter coordinate X for P1: "))
y1 = float(input("Enter coordinate Y for P1: "))
x2 = float(input("Enter coordinate X for P2: "))
y2 = float(input("Enter coordinate Y for P2: "))
d = sqrt((x1-x2)**2 + (y1-y2)**2)
r = d/2
A = pi*r**2
c = 2*pi*r
print("The length of the circle diameter is %.4f."%d)
print("The circle area and circumference are %.4f and %.4f."%(A,c))