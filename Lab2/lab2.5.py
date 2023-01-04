#ITS100 Lecture2 Variables, Input and Output Lab 2.5
four = input("Enter a four-digit integer: ")
four = float(four)
FirstTwo = four//100
LastTwo = four-(FirstTwo*100)
sum = FirstTwo+LastTwo
substract = FirstTwo-LastTwo
value = FirstTwo//LastTwo
remain = FirstTwo%LastTwo
print("The result of %d + %d = %d"%(FirstTwo,LastTwo,sum))
print("The result of %d - %d = %d"%(FirstTwo,LastTwo,substract))
print("The integer value of %d/%d = %d"%(FirstTwo,LastTwo,value))
print("The remainder of %d/%d = %d"%(FirstTwo,LastTwo,remain))
