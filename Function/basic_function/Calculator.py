print("---calculator---")
def calculate(a,b,ch):
    if ch==1:
        return a+b
    elif ch==2:
        return a-b
    elif ch==3:
        return a*b
    elif ch==4:
        return a/b
    else:
        return "enter valid choice"
    
print()
print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")

ch=int(input("enter your choice(1-4)="))
num1=int(input("enter first number="))
num2=int(input("enter second number="))

print("result=",calculate(num1,num2,ch))