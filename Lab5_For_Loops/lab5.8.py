#ITS100 Lecture5 Repetition Structure: For Loops Lab5.8
print("Menu:")
print("===============")
print("A - Americano (50)")
print("E - Espresso (40)")
print("G - Green tea (60)")
print("")
menu = input("Input: ")
print("===============")
ame =0
es= 0
gt = 0
index = 0
for i in menu:
  if i == "A":
    index+=1
    ame +=50
    print("%d. Americano 50"%index)
  elif i == "E":
    index+=1
    es+=40
    print("%d. Espresso 40"%index)
  elif i == "G":
    index+=1
    gt+=60
    print("%d. Green tea 60"%index)
print("===============")
print("Quantity: %d"%index)
total = ame+es+gt
Vat = 0.07*total
gtt = total+Vat
print("Vat: %.2f"%Vat)
print("Total: %.2f"%total)
print("Grand total: %.2f"%gtt)