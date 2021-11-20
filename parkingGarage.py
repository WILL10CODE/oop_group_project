class ParkingGarage():
    def __init__(self, size=100, occupied=50):
        self.size = size
        self.occupied = occupied        
        self.tickets = [range(occupied,size,-1)]
        self.parkingSpaces = [range(occupied,size,-1)]
        self.currentTicket = dict.fromkeys(range(occupied),"Not Paid")

    def parkCar(self):
        print("Welcome to the parking garage. You are being directed to the first available space")
        while True:
            action = input("Would you like to (take) a ticket, (pay) for parking or (leave)")
            if action == "take":
                self.takeTicket()
            elif action == "pay":
                self.payforParking()
            elif action == "leave":
                self.leaveGarage()
                break
            else:
                print("Invalid action. Please take another action")


    def takeTicket(self):
        if self.tickets:
            ticket_num = self.tickets.pop()
            self.currentTicket[self.parkingSpaces.pop()] = "Not Paid"
            print(F"You are parked in space {ticket_num} and received ticket {ticket_num}")
        else:
            print("There are no available spaces")
        return

    def ticketValid(self):
        ticket_num = input("What is your ticket number? ")
        while ticket_num not in self.currentTicket.keys():
            print("Invalid Ticket Number. Input in a valid ticket number")
            self.ticketValid()
        return ticket_num

    def payforParking(self):
        ticket_num = self.ticketValid()
        payment = input("Please put in the dollar amount of your payment for parking:")
        if not payment.isdigit() or int(payment) <= 0:
            print("You have not paid for parking")
        else:
            self.currentTicket[ticket_num] = "Paid"
            print("Thank you for your payment")
        return

    def leaveGarage(self):
        ticket_num = self.ticketValid()
        if self.currentTickets[ticket_num] == "Paid":
            print("Thank You, have a nice day!")
        else:
            print("Please make a payment for parking")
            self.payforParking()
            print("Thank You, have a nice day!")
        self.tickets.append(ticket_num)
        self.parkingSpaces.append(ticket_num)    
        return

    
myparkinggarage = ParkingGarage(200,12)
myparkinggarage.parkCar()
