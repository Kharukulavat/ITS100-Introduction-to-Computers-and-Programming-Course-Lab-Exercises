#Example 6.14
text = input("Input a string: ")
cons = [i for i in text if i.isalpha() if i.lower() not in "aeiou"]
vows = [i for i in text if i.isalpha() if i.lower() in "aeiou"]
print("The number of consonants = %d"%len(cons))
print("The number of vowels = %d"%len(vows))

l = input("Enter the numbers: ").split() # Ex. 2 3 4
print(l) #>> ['2', '3', '4']

list = [1,2,3,4,5,6]
print(list[::-1]) #>> [6, 5, 4, 3, 2, 1]
print(list[:-1]) #>> [1, 2, 3, 4, 5]
print(list[::]) #>> [1, 2, 3, 4, 5, 6]

#Example 6.7
l = []
for i in range(10):
    number = int(input("Enter number%d: "%(i+1)))
    l.append(number)
print(sorted(l, reverse=True))

#We have to use reverse as we use shuffle like this, 
# otherwise it will return 'None' b/c it doesn't create a new reversed list
lst = sorted(l)
lst.reverse()
print(lst)

#if we want to create a new list with reverse elements, 
# we can use slicing with negative step size 
print(l[::-1]) #This will reverse the elements of the list but not sorted