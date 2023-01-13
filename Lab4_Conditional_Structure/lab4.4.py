#ITS100 Lecture4 Conditional structure Lab4.4
letter = input("Enter a single letter: ")
if letter in "ABC":
  print("The digit 2 corresponds to the letter %s on the telephone."%letter)
elif letter in "DEF":
 print("The digit 3 corresponds to the letter %s on the telephone."%letter)
elif letter in "GHI":
 print("The digit 4 corresponds to the letter %s on the telephone."%letter)
elif letter in "JKL":
 print("The digit 5 corresponds to the letter %s on the telephone."%letter)
elif letter in "MNO":
 print("The digit 6 corresponds to the letter %s on the telephone."%letter)
elif letter in "PRS":
 print("The digit 7 corresponds to the letter %s on the telephone."%letter)
elif letter in "TUV":
 print("The digit 8 corresponds to the letter %s on the telephone."%letter)
elif letter in "WXY":
 print("The digit 9 corresponds to the letter %s on the telephone."%letter)
else:
  print("There is no digit on the telephone that corresponds to %s."%letter)