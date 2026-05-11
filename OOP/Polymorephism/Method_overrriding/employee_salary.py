class Employee:

    def salary(self, days):

        per_day = 500
        total = per_day * days

        print("Employee Salary =", total)


class Manager(Employee):

    def salary(self, days):

        per_day = 1500
        total = per_day * days

        print("Manager Salary =", total)


days = int(input("Enter working days: "))

print("1. Employee")
print("2. Manager")

choice = int(input("Enter choice: "))

if choice == 1:

    e = Employee()
    e.salary(days)

elif choice == 2:

    m = Manager()
    m.salary(days)

else:
    print("Invalid Choice")