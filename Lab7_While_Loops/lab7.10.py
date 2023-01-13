#ITS100 Lecture7 While Loops Lab7.10
#Repetition (Nested for-loop, while-loop)
while True:
    num = input("Enter an integer number ('X' to exit) : ")
    if num.isnumeric():
        num = int(num)
        for row in range(num):
            for col in range(num):
                if row == col or int(row)+int(col) == (num-1): 
                    #row == col is to print 'X' in matrix top left to bottom right 
                    #int(row) = int(col) is to print 'X' in matrix top right to bottom left 
                    print("X",end = " ")
                else:
                    print(".",end = " ")
            print()
    elif num == "X":
        break
    else:
        print("")