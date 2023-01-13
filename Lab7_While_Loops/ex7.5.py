#Prime factor
x = input("Input a positive integer here: ")
if x.isnumeric():
    x = int(x)
    print("Prime factor of", x, end=" = ")
    i, factors = 2, [] #Create variables  #Let i = 2 because it is the lowest prime factor so that it could check in below condition
    while i * i <= x: #Because product of prime factor can't exceed the number
        if x % i == 0: #>> i is a prime factor of x 
            x //= i #To divide the number down by i as it already count that i as a prime factor
            factors.append(i)
        else: #When x is odd number
            i += 1  #so that i would continue as odd number ex. 3,5,7,13 #b/c odd number can't be divided by even number!
    if x > 1:
        factors.append(x)
    factors = [str(e) for e in factors] #To update list factors
    print("*".join(factors))
else:
    print("Invalid input") 