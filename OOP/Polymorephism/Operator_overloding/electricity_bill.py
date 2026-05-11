class ElectricityBill:

    def __init__(self,amount):
        self.amount=amount
        
    def __truediv__(self, other):
        total=self.amount/other.amount
        return total
    
total_bill=int(input("enter total bill="))
member=int(input("Enter total family member="))

bill=ElectricityBill(total_bill)
family=ElectricityBill(member)

print("Bill per person=",bill/family)