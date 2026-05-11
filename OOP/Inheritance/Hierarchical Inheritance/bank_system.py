class bank:
    def bank_name(self):
        self.name=input("Enter bank name=")
    

class Saving_acc(bank):

    def saving_data(self):
        amount=float(input("enter amount="))
        interest=0.6*amount
        print()
        print(self.name)
        print("INTEREST RATE =",interest)

class current_acc(bank):

    def current_data(self):
        limit=float(input("enter limit="))
        print(self.name)
        print("LIMIT=",limit)

s=Saving_acc()
s.bank_name()
s.saving_data()        

print()
c=current_acc()
c.bank_name()
c.current_data()