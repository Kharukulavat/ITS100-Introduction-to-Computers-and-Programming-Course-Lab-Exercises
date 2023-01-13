#ITS100 Lecture7 While Loops Lab7.1
l = []
while True:
  word = input("Enter a word:")
  if word[-1] == "y":
    word = word[0:-1] + "ily"
    l.append(word)
  elif word == "exit":
    break
  else:
    l.append(word)
print(l)