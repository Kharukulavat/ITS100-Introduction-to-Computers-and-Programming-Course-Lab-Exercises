#ITS100 Lecture9 Functions Lab9.3
def UserInput():
    while True:
            inp = input("Enter an input: ")
            if inp.isnumeric() and int(inp) >= 0:
                x.append(int(inp))
            elif inp == "Done":
                print("")
                print("The summation is",SumOut())
                print("The minimum is",MinOut())
                print("The maximum is",MaxOut())
                break
            else:
                print("Error")
                break

def SumOut():
    # summation = sum(x)
    # return summation
    return sum(x)

def MinOut():
    # minimum = min(x)
    # return minimum
    return min(x)

def MaxOut():
    # maximum = max(x)
    # return maximum
    return max(x)
    
x = []
UserInput()
