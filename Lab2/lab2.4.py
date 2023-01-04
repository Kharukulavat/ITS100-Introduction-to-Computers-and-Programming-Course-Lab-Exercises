#ITS100 Lecture2 Variables, Input and Output Lab 2.4
Full = input("Input Full Score = ")
Real = input("Input Real Score = ")
Full,Real = float(Full),float(Real)
Percent = (Real/Full)*100
print("----------------------------")
print("--- Calculate Percentage ---")
print("----------------------------")
print("Full Score: %.2f"%Full)
print("Real Score: %.2f"%Real)
print("----------------------------")
print("Percentage: %.2f%%"%Percent)
print("----------------------------")
