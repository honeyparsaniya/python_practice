class electricitybord:

    def board_info(self):

        print("Torent power electricity board\n")

class home(electricitybord):

    def home_bill(self):

        self.unit=float(input("enter unit="))

        if self.unit<=100:

            bill=self.unit*5

        elif self.unit<=300:

            bill=self.unit*7

        else:

            bill=self.unit*10

        print("\n---------home bill---------")
        print("unit consumed=",self.unit)
        print("total bill   =",bill)

class shop(electricitybord):

    def shop_bill(self):

        self.unit=float(input("enter unit="))

        if self.unit<=200:

            bill=self.unit*8
        else:

            bill=self.unit*12

        tax=bill*0.05
        final_bill=bill+tax
        print("\n---------shop bill---------")
        print("unit consumed=",self.unit)
        print("total bill   =",final_bill)

h=home()

print("\n====home electricity bill====")

h.board_info()
h.home_bill()

s=shop()

print("\n=====shop electricity board====")

s.board_info()
s.shop_bill()