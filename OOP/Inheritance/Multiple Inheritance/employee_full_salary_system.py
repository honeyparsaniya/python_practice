#perent class 1
class detail:

    def get_detail(self):

        self.name=input("enter name=")
        self.salary=float(input("enter initial  salary="))

#perent class 2
class bonus:

    def give_bonus(self):

        self.bonus=float(input("enter bonus amount="))

#perent class 3
class tax:

    def give_tax(self):

        self.tax=float(input("enter tax amount="))

#child class
class view_detail(detail,bonus,tax):

    def display(self):

        print("\nNAME=",self.name)
        print("SALARY=",self.salary)
        print("BONUS=",self.bonus)
        print("TAX=",self.tax)

    def calculate(self):

        total=(self.salary+self.bonus)-self.tax

        print("\nTOTAL SALARY=",total)

print("===employee_full_salary_system===\n")

v=view_detail()
v.get_detail()
v.give_bonus()
v.give_tax()
v.display()
v.calculate()