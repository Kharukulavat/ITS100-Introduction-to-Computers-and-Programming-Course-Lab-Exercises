#ITS100 Lecture5 Repetition Structure: For Loops Lab5.6
for i in range(1,6):
  x = int(input("enter a number between 1 and 20: "))
  if 20>= x >= 1:
    if x%2 == 0:
      print("%d is an even number"%x)
    elif x%2 != 0:
      print("%d is an odd number"%x)
  else:
    print("number is invalid")