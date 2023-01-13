#ITS100 Lecture6 Lists Lab6.4
namelist = ["Satawat","Pisit","Thanaphong","Pished","Nut","Amon"]
for i in range(6):
  print("Student list:",namelist)
  delete = input("Please enter a student name that you want to delete (q=exit): ")
  if delete == "q":
    break
  elif delete == "Satawat" or delete == "Pisit" or delete == "Thanaphong" or delete == "Pished" or delete == "Nut" or delete == "Amon":
    print("You will remove '%s' from this class"%delete)
    type = input("Please type (Confirm 'y' , Cancel 'n'): ")
    if type == "y":
      namelist.remove("%s"%delete)