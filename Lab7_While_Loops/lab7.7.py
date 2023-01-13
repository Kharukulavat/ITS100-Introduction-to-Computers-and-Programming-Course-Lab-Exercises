#ITS100 Lecture7 While Loops Lab7.7
print("===================")
print("Cashier Program")
print("===================")
print("")
l = []
while True:
  p = float(input("Enter item price or -1 when finished: "))
  if p == -1:
    break
  else:
    l.append(p)
print("")
print("Total purchase amount is",sum(l))
print("")
pay = float(input("Your payment: "))
print("")
print("You bought %d items today."%len(l))
change = pay-sum(l)
print("Your change is %.2f baht."%change)
  
  
  