#ITS100 Lecture9 Functions Lab9.1
from math import*
def CirArea(x):
    aoc = pi*(x**2)
    return aoc

def SqArea(x):
    aos = x**2
    return aos
    
num = input("Input a positive number: ")
if float(num) > 0:
    num = float(num)
    print("The area of the circle is %.2f"%CirArea(num))
    print("The area of the square is %.2f"%SqArea(num))
else:
    print("Wrong Input")
    