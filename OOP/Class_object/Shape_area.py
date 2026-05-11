class shape:

    def circle(self):
        self.radius=float(input("\nenter radius="))
        print("\narea of circle=",self.radius*3.14)

    def squre(self):
        self.length=int(input("\nenter length of squre="))
        print("\narea of squre=",self.length*self.length)

    def rectangle(self):
        self.length=int(input("\nenter length of rectangle="))
        self.width=int(input("enter width of rectengle="))

        print("area of rectangle=",self.length*self.width)

    def menu(self):
        while True:
            print("1.circle")
            print("2.squre")
            print("3.rectangle")
            print("4.exit")

            ch=int (input("enter your choice="))

            if ch==1:
                self.circle()
            elif ch==2:
                self.squre()
            elif ch==3:
              self.rectangle()
            else:
                print("enter valid choice!")

s1=shape()
s1.menu()