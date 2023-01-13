#ITS100 Lecture4 Conditional structure Lab4.9
pt = int(input("Input parking time (in minutes): "))
hour = pt//60
frac = pt%60
if 60>frac>15:
  hour+=1
charge = hour*20
print("The charge is %d baht."%charge)