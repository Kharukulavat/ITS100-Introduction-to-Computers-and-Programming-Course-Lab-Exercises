#ITS100 Lecture10 Numerical Computing Lab10.5
import numpy as np
from math import*

coor = []
for i in range(1,4):
    co = input("Input coordinate of P%d: "%i).split()
    coor.append(co)
P1 = np.array(coor[0],dtype=float)
P2 = np.array(coor[1],dtype=float)
P3 = np.array(coor[2],dtype=float)

def distance(a,b):
    sumd = 0
    for i in range(len(P1)): #to set the range equal to 3 
        d = (a[i]-b[i])**2
          # same as d = sqrt(pow(a[0]-b[0],2) + pow(a[1]-b[1],2) + pow(a[2]-b[2],2))
        sumd += d
    sumd = sqrt(sumd)  
    return sumd

distances = np.array([distance(P1,P2),distance(P2,P3),distance(P1,P3)]) #To create list with all distances 
maxd = np.max(distances)

print("Output:")
print("The longest distance = %.2f"%maxd)