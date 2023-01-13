#ITS100 Lecture8 Dictionaries & Sets Lab8.2
d = {}
seq = input("Input: ").split()
for i in seq:
  if i.isnumeric():
    i = int(i)
    if i in d:
      d[i] += 1
    else:
      d[i] = 1
for k,v in d.items():
  if k != v:
    gseq = False
    break
  else:
    gseq = True
if gseq == False:
  print("Output: not good sequence")
else:
  print("Output: good sequence")