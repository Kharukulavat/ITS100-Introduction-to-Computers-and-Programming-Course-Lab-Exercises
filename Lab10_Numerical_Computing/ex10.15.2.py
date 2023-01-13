import numpy as np
A = np.array([[5,15,56], [-4,-11,-41], [-1,-3,-11]])
B = np.array([[35],[-26],[-7]])

if np.linalg.det(A) != 0:
    Ainv = np.linalg.inv(A)
    var = np.matmul(Ainv, B)
    print(var)
    print("x = %.1f, y = %.1f, z = %.1f"%(var[0,0], var[1,0], var[2,0]))
else:
    print("We cannot find the solution.")
    
    
