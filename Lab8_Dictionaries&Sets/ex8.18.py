s1 = input("Input string1: ")
s2 = input("Input string2: ")

#Solution 1
list1 = sorted(list(s1.lower()))
list2 = sorted(list(s2.lower()))

#To remove spaces if the inputs have them and check only for alphabets
list1 = [c for c in list1 if c.isalpha()]
list2 = [c for c in list2 if c.isalpha()]

if list1 == list2:
    print("Output: The input strings are anagrams")
else:
    print("Output: The input strings are not anagrams")