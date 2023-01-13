#ITS100 Lecture7 While Loops Lab7.5
x = int(input("Enter an integer number: "))
for i in range(1,x+1):
  for j in range(1,i+1):
    print(j, end=" ") 
  print()
for k in range(x-1,0,-1): #NUMBER OF RANGE IS LOWER AND LOWER BY 1
  for l in range(1,k+1): #SET RANGE OF THIS 
    print(l,end=" ") #PRINT RANGE OF l
  print()