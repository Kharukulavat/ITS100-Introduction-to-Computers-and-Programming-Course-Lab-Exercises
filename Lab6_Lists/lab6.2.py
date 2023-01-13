#ITS100 Lecture6 Lists Lab6.2
x = input("Enter a comma-separated list: ").split(",")
if len(x) >= 3:
  if len(x) == 3:
    print(*x) #to print a list without [ ] 
  else:
    for i in x:
      for j in x:
        for k in x:
          if i<j<k: #so they're not equal and they will arrange in order and can't use the same number because the order will be its own condition 
            print(i,j,k)