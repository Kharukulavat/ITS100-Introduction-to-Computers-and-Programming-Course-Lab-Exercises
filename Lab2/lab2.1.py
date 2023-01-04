#ITS100 Lecture2 Variables, Input and Output Lab 2.1
choc = input("Enter amount of melted chocolate to be poured into the cup (ml): " )
milk = input("Enter amount of milk to be poured into the cup (ml): ")
choc,milk = float(choc),float(milk)
sumofml = choc+milk
sumofoz = sumofml*0.0338
print("Now Emmy's cup is filled with %.2f ml (or about %.2f oz) of chocolate milk."%(sumofml,sumofoz))