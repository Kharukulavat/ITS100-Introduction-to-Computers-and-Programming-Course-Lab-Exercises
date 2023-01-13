#Prime number 
x = int(input("Enter an integer: "))
prime = True
for i in range(2,x):
    if x % i == 0: #when x has non factors, x is a prime otherwise, x is not a prime 
        prime = False
        break #b/c it is not necessary to continue checking the factors
if prime: # >> if prime == True
    print("%d is a prime number."%x)
else:
    print("%d is not a prime number."%x)
    
    
#USING WHILE LOOP
x = int(input("Enter an integer: "))
i = 2
prime = True
#Condition: repeat while i is not a factor of x and i <= x-1
while x % i != 0 and i <= x-1: 
    #print(x, i)
    i += 1
    print("after the loop", x, i)
    
if i == x:
    print("%d is a prime number."%x)
else:
    print("%d is not a prime number."%x)
        