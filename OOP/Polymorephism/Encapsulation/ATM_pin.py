class ATM:

    def __init__(self):
        self.__pin=int(input("enter ATM pin="))
        self.__balance=float(input("enter intial balance="))

    def withdraw(self):

        print("===withdraw amount===")
        pin=int(input("enter pin="))

        if pin==self.__pin:

            amount=float(input("enter amount withdraw="))

            if amount<=self.__balance:

                self.__balance -=amount

                print("\nwithdraw sucessfull")
                print("remmaining balance=",self.__balance)
            else:

                print("amount is more than balance")

        else:

            print("enter valid pin")

a1=ATM()

a1.withdraw()