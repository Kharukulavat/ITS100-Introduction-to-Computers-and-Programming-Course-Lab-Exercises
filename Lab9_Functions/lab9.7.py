#ITS100 Lecture9 Functions Lab9.7
def TriArea(h, b):
    area = 0.5*h*b
    print("The area of the triangle is %.1f"%area)
    
h = float(input("Enter the height (h): "))
b = float(input("Enter the base (b): "))
TriArea(h, b)