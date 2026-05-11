class atm:

    def __init__(self,pin):
        self.pin=pin

    def __eq__(self, value):
        if self.pin==value.pin:
            return "access granted"
        else:
            return "Invalid PIN" 

saved_pin=int(input("create ATM pin="))
entered_pin=int(input("Enter ATM pin="))

p1=atm(saved_pin)
p2=atm(entered_pin)

print(p1==p2)