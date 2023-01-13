#ITS100 Lecture4 Conditional structure Lab4.3
day = float(input("Input number of days: "))
hour = float(input("Input number of hours: "))
print("Please select a choice:")
print("1-to calculate the total number of seconds or 2-to calculate the total number of minutes:")
choice = input("Enter your selected choice: ")
sumofsc = (day*24*60*60) + (hour*60*60)
sumofmn = (day*24*60) + (hour*60)
print("------------------------------------------------")
if choice == "1":
  print("The total number of seconds are %d."%sumofsc)
elif choice == "2":
  print("The total number of minutes are %d."%sumofmn)