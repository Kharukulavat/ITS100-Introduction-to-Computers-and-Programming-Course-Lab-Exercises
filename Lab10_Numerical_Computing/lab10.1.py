#ITS100 Lecture10 Numerical Computing Lab10.1
import numpy as np
size = int(input("Enter the size of matrix: "))
member = []
for i in range(1,size+1):
    for j in range(1,size+1):
        num = int(input("Input element at row %d column %d: "%(i,j)))
        member.append(num)
ar = np.array(member)
matrix = np.reshape(ar, (size,size))

print("")
print("Output:")
print("Matrix =")
print(matrix)

print("Determinant =",np.linalg.det(matrix))

print("Inverse matrix =")
if np.linalg.det(matrix) != 0:
    inv = np.linalg.inv(matrix)
print(inv)


# import numpy as np
# size = int(input())
# member = []
# for i in range(1,size+1):
#     for j in range(1,size+1):
#         num = int(input())
#         member.append(num)
# ar = np.array(member)
# matrix = np.reshape(ar, (size,size))

# print("Output:")
# print(matrix)

# print("Determinant = ",np.linalg.det(matrix))

# print("Inverse matrix = ")
# if np.linalg.det(matrix) != 0:
#     inv = np.linalg.inv(matrix)
# print(inv)