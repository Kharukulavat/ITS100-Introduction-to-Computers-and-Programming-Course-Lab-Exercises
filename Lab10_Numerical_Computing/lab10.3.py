#ITS100 Lecture10 Numerical Computing Lab10.3
import numpy as np
data = np.loadtxt("grades.tsv", delimiter='\t', dtype = float)
id = data[:,0] #Every row in the first column is branch
gpa = data[:,1:] #Every row and every colmun except the first column are sales
credits = np.array([3,2,1,3,3,3])
GPA = np.sum((gpa*credits), axis = 1) / np.sum(credits)
#axis = 1 ; sum every column in the same row
print("Student ID  GPA")
for i in range(data.shape[0]): #Equal to range(20) b/c shape[0] is to count number of rows 
  print("%d  %.2f"%(id[i],GPA[i]))

# import numpy as np
# data = np.loadtxt("grades.tsv", delimiter='\t', dtype = float)
# gpa = data[:,1:]
# credits = np.array([3,2,1,3,3,3])
# GPA = np.sum((gpa*credits), axis = 1) / np.sum(credits)
# #axis = 1 ; sum every column in the same row
# print("Student ID  GPA")
# for i in range(data.shape[0]): #Equal to range(20) b/c shape[0] is to count number of rows 
#   print("%d  %.2f"%(data[i,0],GPA[i]))