class ParkingGarage():
    def __init__(self, size=100, occupied=50, tickets =[]):        
        self.tickets = range(occupied,size)
        self.parkingSpaces =range(occupied,size)
        self.currentTicket = dict.fromkeys(range(occupied),"Not Paid")
        self.size = size
        self.occupied = occupied


    def takeTicket(self):
        if self.tickets:
            self.tickets.pop()
            self.currentTicket[size - self.parkingSpaces.pop()] = "Not Paid"
        else:
            print("There are no available spaces")
        return

    def ticketValid(self):
        ticket_num = input("What is your ticket number? ")
        while ticket_num not in self.currentTicket:
            print("Invalid Ticket Number")
            self.ticketValid()
        return ticket_num

    def payforParking(self):
        ticket_num = self.ticketValid()
        payment = input("Please put in the dollar amount of your payment for parking:")
        if not payment.isdigit():
            print("Invalid entry. Please input in a number of dollars")
            self.payforparking()

        return payment

    def leaveGarage(self):
        ticket_num = self.ticketValid()
        if self.tickets:
            print("Thank You, have a nice day!")
        else:
            print("Please make a payment for parking")
            self.payforParking()
            print("Thank You, have a nice day!")
        self.tickets.append(1)
        self.parkingSpaces.append('available')    
        return

    
    