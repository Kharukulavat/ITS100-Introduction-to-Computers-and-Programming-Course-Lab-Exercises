#ITS100 Lecture6 Lists Lab6.9
a = input("List 1: ").split(",")
b = input("List 2: ").split(",")
x = a+b
wlist = []
for i in x:
  if x.count(i) > 1: #to identify the duplicated number and add to the wlist
    i = int(i)
    wlist.append(i) #but this will add that number for more than one time so we have to remove it until it is that single number left
    for j in wlist: # there will be nu
      if wlist.count(j) != 1: #to remove the duplicated number to be the single one left
        wlist.remove(j)
print(wlist)
