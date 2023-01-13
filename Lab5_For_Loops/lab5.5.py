#ITS100 Lecture5 Repetition Structure: For Loops Lab5.5
line = int(input("enter no. of lines:"))
print(" ")
if line >= 1:
  for i in range(1,line+1):
    if i%2 == 0:
      print("*"*i)
    elif i%2 != 0:
      print("-"*i)
else:
  print("Error")
