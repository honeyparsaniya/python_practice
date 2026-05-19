

balance = 10000

def check_balance():
    return balance

def deposit(amount):
    global balance
    balance += amount
    return balance

def withdraw(amount):
    global balance

    if amount > balance:
        return "Insufficient Balance"

    balance -= amount
    return balance