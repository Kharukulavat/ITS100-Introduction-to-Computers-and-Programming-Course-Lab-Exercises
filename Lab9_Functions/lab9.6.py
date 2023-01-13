#ITS100 Lecture9 Functions Lab9.6
def CelsiusToFahrenheit(c):
    c = float(c)
    fah = (c*(9/5))+ 32
    print("The degree in Fahrenheit is %.2f"%fah)

cel = input("Input temperature in degree Celcius: ")
CelsiusToFahrenheit(cel)