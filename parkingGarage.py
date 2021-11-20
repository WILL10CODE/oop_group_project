class ParkingGarage():
    def __init__(self, size=100, occupied=50, tickets =[]):        
        self.tickets = [1] * (size - occupied)
        self.parkingSpaces = ['available'] * (size - occupied)
        self.currentTicket = dict.fromkeys(["Parked"] * occupied],"Not Paid")
        self.size = size
        self.occupied = occupied


    def takeTicket(self):
        if self.tickets:
            self.tickets.pop()
            self.parkingSpaces.pop()
        else:
            print("There are no available spaces")
        return

    def payforParking(self):
        payment = Input("Please put in the dollar amount of your payment for parking:")
            if not payment.isdigit():
                print("Invalid entry. Please input in a number of dollars")
                self.payforparking()
        return

    def leaveGarage(self):
        return
    