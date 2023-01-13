s1 = input("Input string1: ")
s2 = input("Input string2: ")
list1 = list(s1)
list2 = list(s2)
print(list1)
print(list2)

set1 = set(list1)
set2 = set(list2)

set3 = set1 & set2
print(set3)

print("Output:","".join(sorted(list(set3))))