l = []
while True:
    try:
        x = float(input("Enter a number: "))
        l.append(x)
        if x < 0:
            break
    except ValueError:
        print("Invalid value. Please input an integer!")

print("Input values =",l)