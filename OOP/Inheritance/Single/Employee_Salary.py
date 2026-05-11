#perent class
class employee:

    def __init__(self):
        self.name=input("enter your name=")
        self.id=int(input("enter your ID="))
        print("1.morning")
        print("2.evening")
        print("3.night")

        self.shift=int(input("enter your shift="))
        self.salary=float(input("enter your salary="))
        self.temp=self.salary
#child class
class calculate(employee):
    super().__init__()

    def calculate(self):
        if self.shift==1:
            self.Salary+=10000
        elif self.shift==2:
            self.Salary+=12000
        elif self.shift==3:
            self.Salary+=15000
        else:
            print("Select valid shift")
        
        print("NAME=",self.name)
        print("ID=",self.id)
        print("INITIAL SALARY=",self.temp)
        print("SALARY WITH BONUS=",self.Salary)

print("===your salary counter===")

c=calculate()
c.calculate()