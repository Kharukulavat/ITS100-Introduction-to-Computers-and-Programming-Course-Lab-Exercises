#ITS100 Lecture5 Repetition Structure: For Loops Lab5.9
h = int(input("Height: "))
if h >= 1:
  for i in range(1,h): #create row
    for j in range(0,h-i): # to print "#" equal to the member in range 
      print(end="#") #to make it print in the same line Ex. range(0,4) then it would prints 5 of "#"(equal to the member of range)
    for j in range(1,2*i): # to print "." as odd number (stop at 2*i to make it stop as odd number)
      print(".",end="") # to 
    for j in range(0,h-i): #The same as printing "#""
      print(end= "#")
    print() # to split the line vertically(Make the curser)
  print("."*(h*2-1))
else:
  print("Error")