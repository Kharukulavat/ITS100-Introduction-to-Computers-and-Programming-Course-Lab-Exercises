#ITS100 Lecture7 While Loops Lab7.4
x = int(input("Enter an integer number: "))
for i in range(x):
  for j in range(x):
    if i == 0 or i == x-1 or j == 0 or j == x-1:
      print("x",end=" ")
    else:
      print(" ",end=" ")
  print()