#ITS100 Lecture6 Lists Lab6.1
x = input("Enter a comma-separated list: ").split(",")
for i in range (len(x)): #create the index
  for j in range (len(x)): #create the index
    for k in range (len(x)): #create the index
      if i!=j and i!=k and j!=k: #because permutation of number if one number is used then we have to use the other number left(Not using the same number) so we have to create the condition that the position is not the same
        print(x[i],x[j],x[k]) #to print out the number at that index we checked