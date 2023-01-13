#ITS100 Lecture5 Repetition Structure: For Loops Lab5.3
print("Multiplication table:")
num = input("Please enter a number between 1 to 25: ")
if num.isnumeric():
  num = int(num)
  if 25>= num >= 1:
    print("Multiplication table of %d :"%num)
    for i in range(1,13):
      multi = num*i
      print("%d x %d = %d"%(num,i,multi))
  else:
    print("You entered invalid number")
else:
    print("You entered invalid number")
