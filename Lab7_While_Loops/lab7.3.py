#ITS100 Lecture7 While Loops Lab7.3
x = int(input("Enter an integer number: "))
for i in range(x):
  for j in range(x):
    if i == 0 or i == x-1 or j == 0 or j == x-1:
      print("o",end=" ")
    elif j>=i: #print "x" when Col >= Row 
      print("x",end=" ")
    else:
      print(" ",end=" ") #We have to print " " b/c it can't print that index with leaving those before index get blanked, so we have to print the " " before
  print()

# x = int(input("Enter an integer number: "))

# while True:
#   print("o", end=" ")
#   for i in range(x-2):
#     for j in range(x-2):
#       if i <= j:
#         print("x",end=" ")
#     print()
