class Employee:

    def __init__(self):
        self._salary=float(input("Enter Salary="))

    def bonus(self):

        Bonus=self._salary*0.10
        total=self._salary+Bonus
        print("salary=",self._salary)
        print("bonus=",Bonus)
        print("total salary=",total)

class manager(Employee):

    def show(self):

        print("\nManager access")
        print("salary=",self._salary)

m1=manager()
m1.bonus()
m1.show()
