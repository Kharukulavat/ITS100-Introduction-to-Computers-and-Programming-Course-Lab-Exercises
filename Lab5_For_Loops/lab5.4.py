#ITS100 Lecture5 Repetition Structure: For Loops Lab5.4
import math as m 
num = int(input("Enter an integer number (n>0): "))
print("(1) Factorial of n (n!)")
print("(2) Summation of n integers")
if num > 0:
  op = input("Select operation:")
  print(" ")
  if op == "1":
    fac = m.factorial(num)
    print("Factorial of n (n!) = %d"%fac)
  elif op == "2":
    sum = (num*(num+1))/2
    print("Summation of n integers = %d"%sum)
  else:
    print("N/A Operation!")
else:
  print("Select operation: ")
  print("N/A Operation!")