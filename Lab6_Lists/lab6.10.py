#ITS100 Lecture6 Lists Lab6.10
fruit = input("List of fruits: ").split(",")
for i in fruit:
  if len(i) < 6:
    print(i,"is only %d long!"%(len(i)))
  elif len(i) >= 6:
    print(i,"is 6 characters or more!")