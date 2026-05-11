class bank:

    def __init__(self,bank_name):
        self.bank_name=bank_name

    def show_bank(self):
        print("\n Bank name=",self.bank)

    class Account:

        def __init__(self,acc_no,holder_name,acc_balance):

            self.acc_no=acc_no
            self.holder_name=holder_name
            self.acc_balance=acc_balance

        def deposit(self,amount):

            self.balance +=amount

            print("amount deposit sucessfully")
            print("current balance=",self.balance)

        def show(self):
            print("name=",self.holder_name)
            print("account number=",self.acc_no)
            print("balance=",self.balance)


#user input

bank_name = input("Enter Bank Name: ")
acc_no = input("Enter Account Number: ")
holder_name = input("Enter Holder Name: ")
balance = float(input("Enter Initial Balance: "))
deposit_amount = float(input("Enter Deposit Amount: "))

b1=bank(bank_name)
a1=bank.Account(acc_no,holder_name,balance)

a1.deposit(deposit_amount)

b1.show_bank()
a1.show()