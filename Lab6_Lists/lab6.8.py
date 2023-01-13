#ITS100 Lecture6 Lists Lab6.8

#String concatenate
text = input("Enter a string: ")
x = "" #Define as an empthy string
for i in text: # check for each alphabet
  if i.isupper():
    i = i.lower()
    x += i #Create the reversed string
  elif i.islower():
    i = i.upper()
    x += i
  else: #b/c space is also count as string
    x += i
print("Reverse string output:",x)

#My solution 
text = input("Enter a string: ")
x = []
for i in text: #Check for each alphabet
  if i.isupper():
    i = i.lower()
    x.append(i)
  elif i.islower():
    i = i.upper()
    x.append(i)
  else: #b/c space is also count as string
    x.append(i)
print("Reverse string output:",end=" ")
for i in x:
  print(i,end="")

#Thun's Solution
text = input("Enter a string: ")
list = []
for i in text: #Check for each alphabet
  if i.isupper() == True: #process to collect all the reversed alphabet into the list
    list.append(i.lower()) 
  elif i.islower() == True:
    list.append(i.upper())
  else:
    list.append(i) #Space is also count as member of string
print("Reverse string output:",end=" ")
for i in list:
  print(i,end="")
