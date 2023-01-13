#Create an empthy dictionary
words = {}
while True:
    w = input("Input(DONE = exit): ")
    if w == "DONE":
        break
    if w.lower() in words:
        words[w.lower()] += 1
    else:
        words[w.lower()] = 1
# words = {'ant':2, 'bat':2}
# if a new word 'rat' is input --> {'ant':2, 'bat':2, 'rat':1}
#if an existing word 'ant' is input --> {'ant':3, 'bat':2}

print("Output:")
for k,v in words.items():
    print(k,'=',v)
    
    
#Without using dictionary
# words = [['ant', 2], ['bat', 2]]

# words = ['ant','bat']
# freqs = [2,2]
words = []
while True:
    w = input("Input a string: ")
    if w == "DONE":
        break
    #check if w is in the list "words"
    for v in words:
        if v[0] == w.lower(): #check if key is duplicated 
            v[1] += 1 #plus the value 
            break
    else:
        words.append([w.lower(), 1]) #Add list of [key, value] to the list 
print(words)