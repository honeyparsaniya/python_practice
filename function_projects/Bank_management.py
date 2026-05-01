#bank mangement system

accounts={}
def create_account():
    acc_no=int(input("enter account number:"))
    name=input("enter name:")
    balance=float(input("enter account balance="))
    accounts[acc_no]={"name":name,"balance":balance}
    print("account created succesfully!")

def view_account():
    if not accounts:
        print("not found")
        return
    for acc_no,details in accounts.items():
        print(f"Account={acc_no}, Name={details['name']},Balance={details['balance']}")

def withdraw():
    acc_no=int(input("enter account number="))
    if acc_no in accounts:
        amount=float(input("enter amount to withdraw="))
        if amount <=accounts[acc_no]["balance"]:
            accounts[acc_no]["balance"]-=amount
            print("amount sucessfully withdraw!")
        else:
            print("withdraw amount is more than your balance!")
    else:
        print("account not found!")

def deposit():
    acc_no=int(input("enter account number="))
    if acc_no in accounts:
        amount=float(input("enter amount to deposit="))
        accounts[acc_no]["balance"]+=amount
        print("amount sucessfully deposit to your account!")

def serch_account():
    acc_no=int(input("enter account number="))
    if acc_no in accounts:
        print("account found")
    else:
        print("accound not found")

while True:
    print("---bank management---")
    print("1.create account")
    print("2.view account")
    print("3.deposit amount")
    print("4.withdraw amount")
    print("5.serch account")
    print("6.exit")

    choice=int(input("enter your choice="))

    if choice==1:
        create_account()
    elif choice==2:
        view_account()
    elif choice==3:
        deposit()
    elif choice==4:
        withdraw()
    elif choice==5:
        serch_account()
    elif choice==6:
        break
    else:
        print("please select valid choice")