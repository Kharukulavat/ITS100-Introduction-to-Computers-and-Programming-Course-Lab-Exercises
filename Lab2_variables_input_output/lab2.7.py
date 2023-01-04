#ITS100 Lecture2 Variables, Input and Output Lab 2.7
kg = input("Enter your weight in kg.: ")
cm = input("Enter your height in cm.:  ")
kg,cm = float(kg),float(cm)
pound = kg*2.2046
feet = cm*0.032808399
print(" ")
print("Your weight in pounds = %.2f"%pound)
print("Your height in feet = %.2f"%feet)
