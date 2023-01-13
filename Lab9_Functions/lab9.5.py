#ITS100 Lecture9 Functions Lab9.5
def SeatType():
    while True:
        global price
        seat = input("Select the seat type (P or D or H): ")
        if seat == "P" or seat == "D" or seat == "H":
            if seat == "P":
                price = {"1":100, "2":120}
            elif seat == "D":
                price = {"1":140, "2":200}
            elif seat == "H":
                price = {"1":400, "2":500}
            break
        else:
            print("Wrong seat type! Please select again.")
            continue
        
def MovieType():
    while True:
        global ticketprice
        movie = input("Select the movie type (1 or 2): ")
        if movie == "1" or movie == "2":
            if movie == "1":
                ticketprice = price["1"]
            elif movie == "2":
                ticketprice = price["2"]
            break
        else:
            print("Wrong movie type! Please select again.")
            continue
         
def TicketPrice():
    print("")
    print("The ticket price is",ticketprice)

SeatType()
MovieType()
TicketPrice()

