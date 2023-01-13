#ITS100 Lecture8 Dictionaries & Sets Lab8.4
pair = {}
while True:
  p = input("Input (DONE = exit): ").split()
  if "DONE" in p:
    break
  try:
    if int(p[0]) in pair.keys():
      print("Duplicated ID")
    else:
      pair[int(p[0])] = int(p[1])
  except:
    print("Invalid input")
print("Output:")
score = sorted(pair.values(),reverse = True)
for i in score:
  for key,value in pair.items():
    if i == value: #if we don't check, it will print in many conditions inside the loop b/c we put this dic loop in the score loop 
      print(key,value)