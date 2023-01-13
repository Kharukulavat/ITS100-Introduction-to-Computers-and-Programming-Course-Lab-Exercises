#ITS100 Lecture4 Conditional structure Lab4.10
print("Welcome to Income Tax Computation Program")
income = float(input("Please enter your income (THB): "))
TAX = 0
if income<0:
  print("You are in debt!")
if 15000>=income>0:
  TAX+=0
  net = income-TAX
  print("Tax expense = %.2f"%TAX)
  print("Your net income after tax = %.2f"%net)
elif 50000>=income>15000:
  tax = (income-15000)*0.05
  TAX+=tax
  net = income-TAX
  print("Tax expense = %.2f"%TAX)
  print("Your net income after tax = %.2f"%net)
elif 100000>=income>50000:
  tax = (35000*0.05)+((income-50000)*0.075)
  TAX+=tax
  net = income-TAX
  print("Tax expense = %.2f"%TAX)
  print("Your net income after tax = %.2f"%net)
elif income>100000:
  tax = (35000*0.05)+(50000*0.075)+((income-100000)*0.1)
  TAX+=tax
  net = income-TAX
  print("Tax expense = %.2f"%TAX)
  print("Your net income after tax = %.2f"%net)