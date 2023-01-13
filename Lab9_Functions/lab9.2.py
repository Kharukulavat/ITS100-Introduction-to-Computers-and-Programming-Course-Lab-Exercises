#ITS100 Lecture9 Functions Lab9.2
def LeftRotate():
    for i in range(rot):
        front = leftrot[0] #To define the first of the list
        del leftrot[0] #Then delete that front
        leftrot.append(front) #and then add it to the last of the list
    return leftrot

    # rotate = x[:int(rot)] #list until that number
    # rest = []
    # for i in rotate: #To remove the rotated and create the rest of the list
    #     x.remove(i)
    # for j in x:
    #     rest.append(j)
    # leftrotated = rest + rotate
    # return leftrotated
    
def RightRotate():
    for i in range(rot):
        rightrot.insert(0,rightrot[4]) #to add the last to the front
        del rightrot[5] #and delete the last that we already put it to the front
    return rightrot 

x = input("Enter 5 inputs: ").split()
rot = input("Enter an integer number of rotations (0-4): ")
leftrot = []
rightrot = []
for i in x:
    leftrot.append(i)
    rightrot.append(i)

if rot.isnumeric() and 4 >= int(rot) >= 0:
    rot = int(rot)
    print("The left-rotated list:",LeftRotate())
    print("The right-rotated list:",RightRotate())
else:
    print("Error!")


    