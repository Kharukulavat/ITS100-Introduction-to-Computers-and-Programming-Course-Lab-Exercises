l = []
while True:
    try:
        x = input("Enter a number: ")
        if x == "DONE":
            break
        x = float(x)
        if x > 0:
            l.append(x)
    except ValueError:
        print("Invalid value. Please input an integer!")

print("Sum = %.2f"%sum(l))

#or
l = []
while True:
    try:
        x = input("Enter an integer: ")
        if x == "DONE":
            break
        x = float(x)
        l.append(x)
    except:
        print("Invalid value!")
l = [a for a in l if a>0] #to update list l with only positive integers
print(sum(l))
    
        