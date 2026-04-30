def check_balance(func):
    def wrapper():

        balance=float(input("enter balance="))
        amount=float(input("enter withdraw amount="))

        if amount <= balance:
            func(amount)
        else:
            print("amount is more than balance")
    return wrapper

@ check_balance
def withdraw(amount):
    print(f"{amount} successfully withdraw from your account")

withdraw()