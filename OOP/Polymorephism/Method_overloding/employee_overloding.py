class Employee:

    def salary(self, basic, bonus=0, overtime=0):

        total = basic + bonus + overtime

        print("Total Salary =", total)


e1 = Employee()

print("1. Basic Salary")
print("2. Basic + Bonus")
print("3. Basic + Bonus + Overtime")

choice = int(input("Enter choice: "))

if choice == 1:
    basic = int(input("Enter basic salary: "))
    e1.salary(basic)

elif choice == 2:
    basic = int(input("Enter basic salary: "))
    bonus = int(input("Enter bonus: "))
    e1.salary(basic, bonus)

elif choice == 3:
    basic = int(input("Enter basic salary: "))
    bonus = int(input("Enter bonus: "))
    overtime = int(input("Enter overtime amount: "))
    e1.salary(basic, bonus, overtime)

else:
    print("Invalid Choice")