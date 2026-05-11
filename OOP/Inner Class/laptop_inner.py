class Laptop:

    def __init__(self,brand):
        self.brand=brand

    def show(self):
        print("\nLaptop Brand=",self.brand)

    #inner class
    class processer:

        def __init__(self,company,generation):

            self.compnay=company
            self.generation=generation

        def show_proceser(self):
            print("processer company=",self.company)
            print("generation=",self.generation)

#user input
brand=input("enter brand name=")
company=input("enter company name=")
generation=input("enter generation=")

#outer class
l1=Laptop(brand)

#inner class
p1=Laptop.processer(company,generation)

l1.show()

p1.show_proceser()