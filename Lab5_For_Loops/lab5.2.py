#ITS100 Lecture5 Repetition Structure: For Loops Lab5.2
sum = 0
for i in range(1,6):
  x = int(input("Enter an integer #%d: "%i))
  sum += x
print("The summation is %d."%sum)