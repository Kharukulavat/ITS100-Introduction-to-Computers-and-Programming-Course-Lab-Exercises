import numpy as np

a = np.arange(0,101,1)
print(2**a)

# to make it exactly like the problem
l=[]
a = np.arange(0,101,1)
for i in a:
   l.append("2**%d"%i) 
print(l)