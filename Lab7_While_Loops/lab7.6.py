#ITS100 Lecture7 While Loops Lab7.6
print("===== MAIN MENU ====")
print("1. Addition")
print("2. Subtraction")
print("3. Exit")
print("")
while True:
  op = input("Select an operation (1-3): ")
  if op == "1" or op == "2":
    a,b = input("Enter two numbers: ").split()
    a,b = int(a),int(b)
    add = a+b
    sub = a-b
    if op == "1":
      print(a,"+",b,"=",add)
      print("")
    elif op == "2":
      print(a,"-",b,"=",sub)  
      print("")
  elif op == "3":
    print("Bye!!!")
    break
  
  