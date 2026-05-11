class Bank:

    def create_account(self):
        print("---create your account---")
        self.acc_no = input("Enter Account Number: ")
        self.name = input("Enter Name: ")
        self.balance = int(input("Enter Initial Balance: "))

        print("\nAccount created!")
        print("Account number=",self.acc_no)
        print("name=",self.name)
        print("balance=",self.name)
    
    def deposit(self):
        amount=int(input("\nenter amount="))
        self.balance=self.balance+amount
        print("Amount deposit sucessfully!")
        print("after deposit balance=",self.balance)

    def withdraw(self):
        amount=int(input("\nenter amount="))
        if amount>self.balance:
            print("amount is more than balance!")
        else:
            self.balance=self.balance-amount
            print("Amount withdraw sucessfully!")
            print("balance after withdraw=",self.balance)

    def show_balance(self):
        print("current balance=",self.balance)


    def menu(self):

        while True:

            print("\n---Bank Menu---")
            print("1.deposit")
            print("2.withdrwa")
            print("3.chekc balance")
            print("4.exit")
            
            ch=int(input("\nenter choice(1-4)="))

            if ch==1:
                self.deposit()
            elif ch==2:
                self.withdraw()
            elif ch==3:
                self.show_balance()
            elif ch==4:
                break
            else:
                print("enter valid choice!")

b1=Bank()
b1.create_account()
b1.menu()
