#ITS100 Lecture4 Conditional structure Lab4.2
print("Fever Symptoms Advisor Program")
tem = float(input("Check your body temperature in F = "))
if tem >= 100.4:
  print("You got a fever.")
  treat = input("Choose your treatment : 1 = medication 2 = no medication >>> ")
  if treat == "1":
    print("Take Tylenol every 4 hours as needed")
  elif treat == "2":
    print("Taking a bath in lukewarm water or get the cool packs")
  else:
    print("You choose the wrong choice")
elif tem < 100.4:
  print("You are fine.")