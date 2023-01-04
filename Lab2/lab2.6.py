#ITS100 Lecture2 Variables, Input and Output Lab 2.6
a = input("Enter the 1st number: ")
b = input("Enter the 2nd number: ")
c = input("Enter the 3rd number: ")
a,b,c = float(a),float(b),float(c)
average = (a+b+c)/3
sum = a+b+c
multi = a*b*c
print("a,b,c = %.2f, %.2f, %.2f"%(a,b,c))
print("The average of three integers = %.2f"%average)
print("The summation of three integers = %.2f"%sum)
print("The multiplication of three integers = %.2f"%multi)