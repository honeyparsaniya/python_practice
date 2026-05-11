class mobile:

    def __init__(self,balance):
        self.balance=balance

    def __add__(self,other):
        total=self.balance+other.balance
        return total
    
b1=int(input("Enter first SIM balance="))
b2=int(input("Enter second SIM balance="))

sim1=mobile(b1)
sim2=mobile(b2)

print("Total avilble balance=",sim1+sim2)