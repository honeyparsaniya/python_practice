class Car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed

    def display(self):
        print("===car detail===")
        print("car brand=",self.brand)
        print("car speed=",self.speed)


brand=input("enter car brand name=")
speed=input("enter speed=")

c1=Car(brand,speed)
c1.display()
        