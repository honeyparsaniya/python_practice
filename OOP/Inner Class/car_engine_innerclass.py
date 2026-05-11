class Car:

    def __init__(self, brand):
        self.brand = brand

    def show_car(self):
        print("\nCar Brand:", self.brand)

    class Engine:

        def __init__(self, engine_no, horsepower):
            self.engine_no = engine_no
            self.horsepower = horsepower

        def mileage(self):
            if self.horsepower > 150:
                print("Mileage: 15 KM/L")
            else:
                print("Mileage: 22 KM/L")

        def show_engine(self):
            print("Engine Number:", self.engine_no)
            print("Horsepower:", self.horsepower)


# User Input
brand = input("Enter Car Brand: ")
engine_no = input("Enter Engine Number: ")
horsepower = int(input("Enter Horsepower: "))

c1 = Car(brand)
e1 = Car.Engine(engine_no, horsepower)

c1.show_car()
e1.show_engine()
e1.mileage()