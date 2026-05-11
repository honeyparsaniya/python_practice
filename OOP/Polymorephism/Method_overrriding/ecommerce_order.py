class Order:

    def delivery(self, amount):

        charge = 40
        total = amount + charge

        print("Normal Delivery Selected")
        print("Product Amount =", amount)
        print("Delivery Charge =", charge)
        print("Final Bill =", total)


class ExpressOrder(Order):

    def delivery(self, amount):

        charge = 120
        total = amount + charge

        print("Express Delivery Selected")
        print("Product Amount =", amount)
        print("Delivery Charge =", charge)
        print("Final Bill =", total)


amount = int(input("Enter product amount: "))

print("1. Normal Delivery")
print("2. Express Delivery")

choice = int(input("Enter choice: "))

if choice == 1:

    o = Order()
    o.delivery(amount)

elif choice == 2:

    e = ExpressOrder()
    e.delivery(amount)

else:
    print("Invalid Choice")