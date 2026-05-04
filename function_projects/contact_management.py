#contact management system
contacts={}

def add_contacts():
    name=input("enter name=")
    phone=int(input("enter phone number="))
    contacts[name]=phone
    print("saved sucessfully")

def view_contacts():
    if not contacts:
        print("storage is empty")
    for name,phone in contacts.items():
        print(f"{name}:{phone}")

def serch_contacts():
    name=input("enter name=")
    if name in contacts:
        print(f"phone number ={contacts[name]}")
    else:
        print("not found")

def delete_contacts():
    name=input("enter name=")
    if name in contacts:
        del contacts[name]
        print("contacts delete sucessfully")
    else:
        print("not found")


while True:
    print("\n===contact management system===")
    print("1.add contact")
    print("2.view contact")
    print("3.serch contact")
    print("4.delete contact")
    print("5.exit")
    choice=int(input("enter choice(1-5)"))

    if choice==1:
        add_contacts()
    elif choice==2:
        view_contacts()
    elif choice==3:
        serch_contacts()
    elif choice==4:
        delete_contacts()
    elif choice==5:
        break
    else:
        print("enter valid choice")
