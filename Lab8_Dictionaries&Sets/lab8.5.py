#ITS100 Lecture8 Dictionaries & Sets Lab8.5
words = {}
sen = input("Input a sentence: ").split()
for i in sen:
  if i.lower() in words:
    words[i.lower()] += 1
  else:
    words[i.lower()] = 1
print("Output:")
for key,value in words.items():
  if value > 1:
    print(key)
if max(words.values()) == 1: #to check if max is 1 (no any duplicated words)
  print("none")
