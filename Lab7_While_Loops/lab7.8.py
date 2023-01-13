#ITS100 Lecture7 While Loops Lab7.8
even = []
odd = []
while True:
  x = int(input("Enter an integer (0 to exit): "))
  if x == 0:
    break
  elif x%2 == 0:
    even.append(x)
  else:
    odd.append(x)
print("----------------------------------")
print("The number of even integers is %d"%len(even))
print("The number of odd integers is %d"%len(odd))