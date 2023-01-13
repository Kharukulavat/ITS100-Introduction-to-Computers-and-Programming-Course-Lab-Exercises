s = input("Enter a string: ")
for c in s:
    if c.lower() in "aeiou":
        continue
    print(c, end="")
print() #To move the cursor to the next line so that it can print the next code in the right order because we end the previous code with parameter end(end="") 

#Or if we don't use continue
s = input("Enter a string: ")
for c in s:
    if c.lower() not in "aeiou": #We can use 'not in' instead
        print(c, end="")
print()