print("---CALCULATOR")
num1=int(input("enter first number="))
num2=int(input("enter second number="))

print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")

ch=int(input("enter  your choice="))

if ch==1:
    print("addition=",num1+num2)
elif ch==2:
    print("substraction=",num1-num2)
elif ch==3:
    print("multiplication=",num1*num2)
elif ch==4:
    if num2==0:
        print("not divsible by 0")
    else:
        print("division=",num1/num2)
else :
    print("enter valid choice")