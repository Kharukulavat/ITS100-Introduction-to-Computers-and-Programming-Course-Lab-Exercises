#ITS100 Lecture8 Dictionaries & Sets Lab8.6
pair = {}
while True:
  try:
    x = input("Input (DONE = exit): ").split()
    if "DONE" in x:
      break
    else:
      pair[int(x[0])] = int(x[1])
  except:
    print("Invalid input")
print("Output:")
score = sorted(pair.values(),reverse = True) #List of sorted score
for i in score:
  for key, value in pair.items():
    if i == value: #if we don't check, it will print in many conditions inside the loop b/c we put this dic loop in the score loop 
      print(key,value)