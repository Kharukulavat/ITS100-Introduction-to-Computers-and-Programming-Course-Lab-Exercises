#ITS100 Lecture7 While Loops Lab7.2
l = []
while True:
  word = input("Enter a name:")
  if word == "exit":
    break
  else:
    l.append(word.capitalize())
print(l)