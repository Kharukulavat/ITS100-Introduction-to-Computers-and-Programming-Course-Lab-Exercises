#ITS100 Lecture8 Dictionaries & Sets Lab8.3
inp1 = input("Input sequence1: ").split()
inp2 = input("Input sequence2: ").split()
seq1 = set()
seq2 = set()
for i in inp1:
  if i.isnumeric():
    seq1.add(i)
for i in inp2:
  if i.isnumeric():
    seq2.add(i)
if seq1==seq2:
  print("Output: same set")
else:
  print("Output: different set")
  
    