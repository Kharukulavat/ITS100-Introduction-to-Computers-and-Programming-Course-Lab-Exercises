#ITS100 Lecture2 Variables, Input and Output Lab 2.2
x = input("Enter x: ")
y = input("Enter y: ")
x,y = float(x),float(y)
Aot = (1/2)*x*(y-(0.8*y))
Aor = 0.8*y*(x/2)
A = Aot+Aor
print("Total area of the shape is %.2f square units."%A)