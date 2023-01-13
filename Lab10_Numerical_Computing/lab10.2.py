#ITS100 Lecture10 Numerical Computing Lab10.2
import numpy as np
member = []
xyz = []
for i in range(1,13):
    cv = int(input("Input C%d: "%i))
    if i!=  4 and i != 8 and i!= 12:
        member.append(cv)
    else:
        xyz.append(cv)
matrix = np.array(member)
xyz = np.array(xyz)

matrix = np.reshape(matrix, (3,3))

if np.linalg.det(matrix) != 0:
    inv = np.linalg.inv(matrix)
else:
  print("Unable to find a solution")

xyz = np.matmul(inv, xyz)

print("Solution:")
print("x = %.2f"%xyz[0])
print("y = %.2f"%xyz[1])
print("z = %.2f"%xyz[2])

