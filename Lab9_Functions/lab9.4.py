#ITS100 Lecture9 Functions Lab9.4
def UserInput():
    global weight,height
    weight = float(input("Input your weight (kilogram): "))
    height = float(input("Input your height (meter): "))
    
def FindBMI(hh,ww):
    BMI = weight/(height**2)
    return BMI

def ShowBMI(MyBMI):
    print("The user BMI is %.2f"%MyBMI)
    
UserInput()
ShowBMI(FindBMI(weight,height))