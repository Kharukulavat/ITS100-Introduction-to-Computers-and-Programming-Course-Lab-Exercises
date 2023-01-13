F = [0,1] #1 1 2 3 5 8 ....
while True:
    f = F[-1] + F[-2]
    if f <= 100:
        F.append(f)
    else:
        break
print("Fibonacci sequence =", F)

#Or we can stop when it exceeds 100 then delete the last index later.
F = [0,1] #1 1 2 3 5 8 ....
while True:
    f = F[-1] + F[-2]
    if f > 100:
        del F[-1]
        break
print("Fibonacci sequence =", F)