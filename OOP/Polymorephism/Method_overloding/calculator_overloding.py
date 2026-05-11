class Calculator:

    def calculate(self, a, b=0, c=0):

        if b == 0 and c == 0:
            print("Square =", a * a)

        elif c == 0:
            print("Addition =", a + b)

        else:
            print("Total =", a + b + c)


c1 = Calculator()

print("1. Square")
print("2. Addition")
print("3. Total Sum")

choice = int(input("Enter choice: "))

if choice == 1:
    n = int(input("Enter number: "))
    c1.calculate(n)

elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c1.calculate(a, b)

elif choice == 3:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    c1.calculate(a, b, c)

else:
    print("Invalid Choice")