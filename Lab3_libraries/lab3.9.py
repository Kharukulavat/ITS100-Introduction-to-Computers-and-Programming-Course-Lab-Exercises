#ITS100 Lecture3 Libraries Lab3.9
import math
wc = float(input("Enter the width of the cube: "))
wcon = float(input("Enter the width of the container: "))
hcon = float(input("Enter the height of the container: "))
dcon = float(input("Enter the depth of the container: "))
dimension1 = math.floor(wcon / wc)
dimension2 = math.floor(hcon / wc)
dimension3 = math.floor(dcon / wc)
number_of_cubes = dimension1 * dimension2 * dimension3
print("The number of cubes that can fit into the container is %d."%number_of_cubes)