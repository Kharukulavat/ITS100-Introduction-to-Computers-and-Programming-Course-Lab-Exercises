s = input("Input a string: ")
alphabets = {}
for c in s:
    if c.isalpha():
        if c.lower(): #We don't have to check if it's in dictionary or not if we add this
            alphabets[c.lower()] = 1
print("Output: ", end="")
for k in sorted(alphabets.keys()):
    print(k, end="")
print()
# print("Output:","".join(sorted(alphabets.keys()))) also has the same output

    
        