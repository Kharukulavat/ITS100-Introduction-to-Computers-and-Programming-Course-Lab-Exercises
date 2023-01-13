#ITS100 Lecture3 Libraries Lab3.10
import math
cmsqr = float(input("Input the covered area for one paint bottle (cm square): "))
numsp = float(input("Input the number of the spheres: "))
r = float(input("Input the radius of each sphere (cm): "))
A = 4*(math.pi)*r**2
numpbt = (numsp*A)/cmsqr
bottles = math.ceil(numpbt)
print("The paint bottles are needed to paint the surface of spheres is %d."%bottles)