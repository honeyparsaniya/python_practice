#perent class (level 1)
class user:

    def get_detail(self):

        self.name=input("enter name=")
        self.city=input("enter city=")

class order(user):

    def get_order(self):

        self.p_name=("enter product name=")
        self.p_price=float(("enter product price="))

class display(order):

    def delivery_charge(self):

        self.d_charge=float(input("enter delivery charge="))
        total=self.p_price+self.d_charge

    def show_detail(self):

        print("===user detail===")
        print("=n")