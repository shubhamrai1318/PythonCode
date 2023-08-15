class Ticket:
    def __init__(self, name, status, seat):
        self.name = name
        self.status = status
        self.seat = seat

    def doBooking(self):
        self.name = input("Enter Name: ")
        self.status = "booked"

    def isSeatBooked(self):
        if self.status == "empty":
            return False
        else:
            return True

    def __str__(self):
        return "Name = {0} , Status = {1} , seat = {2}".format(self.name, self.status, self.seat)


seats = {}
for i in range(1, 11):
    t = Ticket(" ", "empty", i)
    seats[i] = t

while True:
    c = int(input(" 0=Exit 1=Booking, 2=Booked Seats : "))
    if c == 0:
        break
    if c == 1:
        n = int(input("Which seat You want to book: "))
        if not seats[n].isSeatBooked():
            seats[n].doBooking()
            print(seats[n])
        else:
            print("Already Booked")

    if c==2:
        for i in range(1,11):
            if seats[i]=='Booked':
                print(seats[i])
