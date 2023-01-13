#ITS100 Lecture9 Functions Lab9.8
def myRange(FirstVal, UpperBound, StepSize):
    Range = []
    for i in range(FirstVal,UpperBound,StepSize):
        Range.append(i)
    print("Range =",Range)
    
FirstVal = int(input("Enter the first number: "))
UpperBound = int(input("Enter the upper bound: "))
StepSize = int(input("Enter the step: "))
myRange(FirstVal, UpperBound, StepSize)
    