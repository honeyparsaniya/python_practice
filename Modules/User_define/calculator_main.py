import mymodule

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Choose Operation: "))

if choice == 1:
    print("Answer =", mymodule.add(a, b))

elif choice == 2:
    print("Answer =", mymodule.subtract(a, b))

elif choice == 3:
    print("Answer =", mymodule.multiply(a, b))

elif choice == 4:
    print("Answer =", mymodule.divide(a, b))

else:
    print("Invalid Choice")