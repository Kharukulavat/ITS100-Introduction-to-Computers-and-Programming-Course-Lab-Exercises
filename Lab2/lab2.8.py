#ITS100 Lecture2 Variables, Input and Output Lab 2.8
x = input("Enter the first integer number: ")
y = input("Enter the second integer number: ")
x,y = int(x),int(y)
sum = x+y
sub = x-y
product = x*y
quo = x/y
print(" ")
print("The sum is %d"%sum)
print("The difference is %d"%sub)
print("The product is %d"%product)
print("The quotient is %d"%quo)