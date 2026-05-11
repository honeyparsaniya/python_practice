def addition():

    num1=int(input("enter a first number="))
    num2=int(input("enter second number="))

    add=num1+num2

    print("addition=",add)

def substraction():

    num1=int(input("enter a firdt number="))
    num2=int(input("enter a second number ="))
    
    sub=num1-num2

    print("substraction=",sub)

def multiplication():

    num1=int(input("enter a first number="))
    num2=int(input("enter a second number="))

    mul=num1*num2

    print("multiplication=",mul)

print("1.addition")
print("2.substraction")
print("3.multiplication")

ch=int(input("enter a choice="))

if ch==1:

    addition()

elif ch==2:

    substraction()

elif ch==3:

    multiplication()

else:

    print("select valid choice")
