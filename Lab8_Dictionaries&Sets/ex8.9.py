#Example 8.9

#Without using dictionary
s = input("Input a string: ")
a,e,i,o,u = 0,0,0,0,0
for c in s:
    if c.lower() == 'a':
        a += 1
    elif c.lower() == 'e':
        e += 1
    elif c.lower() == 'i':
        i += 1
    elif c.lower() == 'o':
        o += 1
    elif c.lower() == 'u':
        u += 1
print("Output:")
print("A =", a)
print("E =", e)
print("I =",i)
print("O =", o)
print("U =", u)

#With using dictionary
vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
for c in s:
    if c.lower() in 'aeiou':
        vowels[c.lower()] += 1
print("Output:")
for k,v in vowels.items():
    print(k.upper(),"=",v)
    
   