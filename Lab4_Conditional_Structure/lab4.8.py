#ITS100 Lecture4 Conditional structure Lab4.8
print("welcome to pizza online ordering.")
print('please input "y" if you want to order, otherwise input "n"')
pizza = input("pizza? (price_359): ") 
chic = input("chicken? (price_3 pieces for 199): ")
pasta = input("pasta? (price_99): ")
salad = input("salad? (price_99): ") 
coke = input("coke? (price_550 ml for 25): ")

if pizza == "y":
  pizza = 359
else: 
  pizza = 0
if chic == "y":
  chic = 199
else:
  chic = 0
if pasta == "y":
  pasta = 99
else:
  pasta = 0
if salad == "y":
  salad = 99
else:
  salad = 0
if coke == "y":
  coke = 25
else:
  coke = 0
price = pizza+chic+pasta+salad+coke
print("total price is %d"%price) 
print("thanks")