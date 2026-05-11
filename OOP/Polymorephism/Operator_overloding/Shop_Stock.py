class shop:

    def __init__(self,stock):
        self.stock=stock

    def __sub__(self, other):
        total=self.stock-other.stock
        return total

total_stock=int(input("Enter Total Stock="))
total_sold=int(input("Enter Sold Stock="))

s1=shop(total_stock)
s2=shop(total_sold)

print("remainning stock=",s1-s2)