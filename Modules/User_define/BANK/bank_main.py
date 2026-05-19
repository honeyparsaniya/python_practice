import bankmodule

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")

choice = int(input("Enter Choice: "))

if choice == 1:
    print("Balance =", bankmodule.check_balance())

elif choice == 2:

    amount = int(input("Enter Deposit Amount: "))
    print("Updated Balance =", bankmodule.deposit(amount))

elif choice == 3:

    amount = int(input("Enter Withdraw Amount: "))
    print("Updated Balance =", bankmodule.withdraw(amount))

else:
    print("Invalid Choice")