#ITS100 Lecture8 Dictionaries & Sets Lab8.1
word = {}
text = input("Input: ").split()
for i in text:
  if i.lower() in word:
    word[i.lower()] += 1
  else:
    word[i.lower()] = 1
print("Output:")
for key,value in word.items():
  if value == max(word.values()):
    print(key,"=",value)