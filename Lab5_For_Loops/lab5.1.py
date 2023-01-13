#ITS100 Lecture5 Repetition Structure: For Loops Lab5.1
even = 0
odd = 0
for i in range(1,6):
  x = int(input("enter a number "))
  if x%2 == 0:
    even += 1
  elif x%2 != 0:
    odd += 1
print("there were %d even numbers"%even)
print("there were %d odd numbers"%odd)
    