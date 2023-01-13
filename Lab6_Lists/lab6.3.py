#ITS100 Lecture6 Lists Lab6.3
list = []
for i in range(5):
  x =int(input("Input#%d: "%(i+1)))
  list.append(x)
sum = sum(list) 
avr = sum/5
min = min(list)
max = max(list)
op = input("Select the option: 1)Summary,2)average,3)min,4)max....")
if op == "1":
  print("Your result is %d"%sum)
elif op == "2":
  print("Your result is %d"%avr)
elif op == "3":
  print("Your result is %s"%min)
elif op == "4":
  print("Your result is %s"%max)