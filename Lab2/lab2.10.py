#ITS100 Lecture2 Variables, Input and Output Lab 2.10
ITS100 = input("enter grade from ITS100: ")
EL171 = input("enter grade from EL171: ")
SCS183 = input("enter grade from SCS183: ")
ITS100,EL171,SCS183 = float(ITS100),float(EL171),float(SCS183)
GPA = ((3*ITS100)+(3*EL171)+(SCS183))/(3+3+1)
print(" ")
print("Your GPA is %.2f"%GPA)
