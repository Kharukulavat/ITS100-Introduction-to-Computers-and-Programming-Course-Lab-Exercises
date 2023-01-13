#ITS100 Lecture4 Conditional structure Lab4.6
print("===============================")
x = float(input("Input x = "))
y = float(input("Input y = "))
x1,y1 = 0,0
x2,y2 = 2,0
x3,y3 = 1,2
alpha = ((y2-y3)*(x-x3)+(x3-x2)*(y-y3))/((y2-y3)*(x1-x3)+(x3-x2)*(y1-y3))
beta = ((y3-y1)*(x-x3)+(x1-x3)*(y-y3))/((y2-y3)*(x1-x3)+(x3-x2)*(y1-y3))
gamma = 1-alpha-beta
if alpha > 0 and beta > 0 and gamma > 0:
  print("Point(x,y) inside polygon")
else:
  print("Point(x,y) outside polygon")