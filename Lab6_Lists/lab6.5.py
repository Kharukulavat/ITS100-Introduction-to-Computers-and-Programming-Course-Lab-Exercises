#ITS100 Lecture6 Lists Lab6.5
x = int(input("How many persons in a group? : "))
list = []
for i in "ABC":
  print("Please enter grade from group",i)
  for j in range(x):
    grade = float(input("enter grade: "))
    list.append(grade)
lista = list[:x] #Ex. if x = 3; position 1 to 3 (Index 0 to 2)
listb = list[x:2*x] #position 4 to 6 (Index 3 to 5) 
listc = list[2*x:] #position 7 to 9 (Index 6 to 8)
print("the highest grade of group A is",max(lista))
print("the highest grade of group B is",max(listb))
print("the highest grade of group C is",max(listc))