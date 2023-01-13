#ITS100 Lecture6 Lists Lab6.6
text = input("Enter dd/mm/yyyy: ")
if text.isnumeric():
  if len(text) == 8:
    month = text[2:4]
    month = int(month)
    if 12>= month > 0:
      print("Date =",text[0:2])
      print("Month = %d"%month)
      year = text[4:]
      year = int(year)
      cyear = year-543
      print("Year =",cyear)
    else:
      print("Error! There're 12 months")
  else:
    print("Please enter 8 digits!!")
    