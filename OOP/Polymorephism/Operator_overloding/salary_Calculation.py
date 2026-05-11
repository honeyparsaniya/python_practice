class Salary:

    def __init__(self,salary):
        self.salary=salary

    def __mul__(self, other):
        total=self.salary*other.salary
        return total

working_day=int(input("Enter working days="))
perDay_salary=int(input("Enter per day salary="))

s1=Salary(working_day)
s2=Salary(perDay_salary)

print("Total salary=",s1*s2)