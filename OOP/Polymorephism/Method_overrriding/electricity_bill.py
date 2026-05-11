class ElectricityBill:

    def bill(self, units):

        amount = units * 5

        print("Residential Connection")
        print("Total Bill =", amount)


class CommercialBill(ElectricityBill):

    def bill(self, units):

        amount = units * 8

        print("Commercial Connection")
        print("Total Bill =", amount)


units = int(input("Enter electricity units: "))

print("1. Residential")
print("2. Commercial")

choice = int(input("Enter choice: "))

if choice == 1:

    r = ElectricityBill()
    r.bill(units)

elif choice == 2:

    c = CommercialBill()
    c.bill(units)

else:
    print("Invalid Choice")