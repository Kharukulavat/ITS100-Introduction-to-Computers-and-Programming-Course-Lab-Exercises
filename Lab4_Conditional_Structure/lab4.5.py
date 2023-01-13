#ITS100 Lecture4 Conditional structure Lab4.5
money = int(input("Please specify amount of money you would like to withdraw:"))
fivehd = money//500
onehd = (money-(fivehd*500))//100
ftb = (money-(fivehd*500)-(onehd*100))//50
twob = (money-(fivehd*500)-(onehd*100)-(ftb*50))//2
oneb = (money-(fivehd*500)-(onehd*100)-(ftb*50)-(twob*2))
print("we may give you:")
print("%d bill(s) of 500 bath"%fivehd)
print("%d bill(s) of 100 bath"%onehd)
print("%d bill(s) of 50 bath"%ftb)
print("%d coin(s) of 2 bath"%twob)
print("%d coin(s) of 1 bath"%oneb)