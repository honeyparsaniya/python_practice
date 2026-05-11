class Parking:

    def parking_fee(self, hours):

        fee = hours * 20

        print("Bike Parking Fee =", fee)


class CarParking(Parking):

    def parking_fee(self, hours):

        fee = hours * 50

        print("Car Parking Fee =", fee)


hours = int(input("Enter parking hours: "))

print("1. Bike Parking")
print("2. Car Parking")

choice = int(input("Enter choice: "))

if choice == 1:

    b = Parking()
    b.parking_fee(hours)

elif choice == 2:

    c = CarParking()
    c.parking_fee(hours)

else:
    print("Invalid Choice")