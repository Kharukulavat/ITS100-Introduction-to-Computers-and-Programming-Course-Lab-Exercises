#ITS100 Lecture4 Conditional structure Lab4.7
money = float(input("Enter money you have: "))
price = float(input("Enter price of item: "))
Tax = 0.08*price
total = price+Tax
short = total-money
print("Tax: %d"%Tax)
print("Total price : %d"%total)
if money < total:
  print("You have shortfall of %d, you cannot buy."%short)
else:
  print("yes you have enough money to buy")