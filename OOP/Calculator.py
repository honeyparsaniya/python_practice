class claculator:

    def numbers(self):
        print("---enter numbers---")
        self.num1=int(input("enter first number="))
        self.num2=int(input("enter second number="))

    def add(self):
        print("---add two number---")
        sum=self.num1+self.num2
        print("\naddition=",sum)

    def sub(self):
        print("---substract two number---")
        sum=self.num1-self.num2
        print("\nsubstraction=",sum)
    
    def mul(self):
        print("---multiply two value---")
        sum=self.num1*self.num2
        print("\nmultiplication=",sum)

    def div(self):
        print("---divide two value---")
        if self.num2<=0:
            print("second value is 0,so not divisible")
        else:
            sum=self.num1/self.num2
            print("division=",sum)

    def menu(self):

        while True: 

            print("---\nCALCULATOR---")
            print("1.addition")
            print("2.substraction")
            print("3.multiplication")
            print("4.division")
            print("5.exit")

            ch=int(input("enter your choice="))

            if ch==1:
                self.add()
            elif ch==2:
                self.sub()
            elif ch==3:
                self.mul()
            elif ch==4:
                self.div()
            elif ch==5:
                break
            else:
                print("enter valid choice!")

c1=claculator()

c1.numbers()
c1.menu()