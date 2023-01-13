#ITS100 Lecture4 Conditional structure Lab4.1
print("========Welcome to Hi!! Car Wash========")
serv = input("Choose your services: W=Wash C=Wash+Vacuum >>> ") 
serv =serv.upper()
if serv == "W":
  size = input('Enter your car size: "S", "M", "L" : ')
  size=size.upper()
  if size == "S":
    print("Price = 100 Baht")
  elif size == "M":
    print("Price = 120 Baht")
  elif size == "L":
    print("Price = 140 Baht")
  else:
    print("You Enter the wrong car size")
elif serv == "C":
  size = input('Enter your car size: "S", "M", "L" : ')
  size=size.upper()

  if size == "S":
    print("Price = 120 Baht")
  elif size == "M":
    print("Price = 140 Baht")
  elif size == "L":
    print("Price = 160 baht")
  else:
    print("You Enter the wrong car size")
else:
  print("Please Choose Your Services")