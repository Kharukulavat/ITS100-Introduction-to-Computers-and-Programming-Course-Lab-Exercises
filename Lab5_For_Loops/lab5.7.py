#ITS100 Lecture5 Repetition Structure: For Loops Lab5.7
Like = 0
Sad = 0
Heart = 0
for i in range(1,11):
  fl = input('Feeling Like ("L"), Sad ("S"), and Heart("H")? ')
  if fl in "LSH":
    if fl == "L":
      Like+=1
    elif fl == "S":
      Sad+=1
    elif fl == "H":
      Heart+=1
  else:
    print("Invalid input, accepts only (L/S/H).")
print("============")
Total = Like+Sad+Heart
plike = (Like/Total)*100
psad = (Sad/Total)*100
pheart = (Heart/Total)*100
print("Total is %d"%Total)
print("============")
print("Like: %d (%.2f%%)"%(Like,plike))
print("Sad: %d (%.2f%%)"%(Sad,psad))
print("Heart: %d (%.2f%%)"%(Heart,pheart))
