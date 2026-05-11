#perent class 1
class get_food:

    def food_cost(self):

        self.cost=float(input("enter food charge="))

class delivery:

    def del_charge(self):

        self.charge=float(input("enter delivery charge="))

class bill(get_food,delivery):

    def total_bill(self):

        total=self.cost+self.charge

        print("Total Bill=",total)

print("===food bill system===")

b=bill()
b.food_cost()
b.del_charge()
b.total_bill()