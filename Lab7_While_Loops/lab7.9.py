#ITS100 Lecture7 While Loops Lab7.9
l = []
while True:
  x = int(input("Enter an integer (-1 to exit): "))
  if x == -1:
    break
  else:
    l.append(x)
print("The sum of %d numbers is %d."%(len(l),sum(l)))