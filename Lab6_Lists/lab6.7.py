#ITS100 Lecture6 Lists Lab6.7
import random as r 
list = []
for i in range(4):
  x = input("Enter string#%d: "%(i+1))
  list.append(x)
r.shuffle(list)
print("Random order of sentence:",*list)