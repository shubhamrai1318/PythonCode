seats = {1: (), 2: (), 3: (), 4: (), 5: ()}
"""
trains={1:{},2:{}

"""

# seats
def exit():
    print("You have selected Exit option")


def book(n):
    print("Welcome To Booking Menu ")
    n = int(input("Enter the Seat No. you want to book: "))
    if n < 6:
        if seats[n] == ():
            name = input("Name: ")
            phn = (input("Mob_no: "))
            #for i in range(1, 6):
            seats[n] = ["Name:", name, "Mob_no: ", phn]
        # print(seats)
        else:
            print("Seat Already Booked")
    else:
        print("Only 6 Seats are Available in this Train")


def cancel(n):
    print(seats)
    n = int(input("Which Seat You want to Cancel :"))
    #for i in range(1, 6):
    seats[n] = ()


def check_ticket(n):
    n = int(input("Enter Seat Number: "))
    print(seats[n])


def all_ticket(n):
    for key in seats.keys():
        value = seats[key]
        if value != ():
            print(key, value)


while True:
    print("\n0-Exit, 1-Book, 2-Cancel, 3-Check Ticket, 4-All Ticket Status")
    n = int(input("Enter Your Choice: "))
    if n == 0:
        break
    if n == 1:
        book(n)
    if n == 2:
        cancel(n)
    if n == 3:
        check_ticket(n)
    if n == 4:
        all_ticket(n)
    if n > 4:
        print("Wrong Choice\t Try Again")
