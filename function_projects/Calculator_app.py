def add():
    a=float(input("enter first value="))
    b=float(input("enter second value="))
    print("sum=",a+b)

def sub():
    a=float(input("enter first value="))
    b=float(input("enter second value="))
    print("substraction=",a-b)

def mul():
    a=float(input("enter first value="))
    b=float(input("enter second value="))
    print("multiplication=",a*b)

def div():
    a=float(input("enter first value="))
    b=float(input("enter second value="))
    if b!=0:
        print("division=",a/b)
    else:
        print("second  value is zero,so no divisible")

while True:
    print("===your calculator===")
    print("1.addition")
    print("2.substraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")
    choice=int(input("enter choice(1-5)="))

    if choice==1:
        add()
    elif choice==2:
        sub()
    elif choice==3:
        mul()
    elif choice==4:
        div()
    elif choice==5:
        break
    else:
        print("enter valid choice!")