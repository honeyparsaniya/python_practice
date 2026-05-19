import math

print("1.squre")
print("2.circle")
print("rectangle")
ch=int(input("enter choice="))

if ch==1:
    num=float(input("enter length="))
    print("area of squre=",num*num)
elif ch==2:
    num=float(input("Enter radius="))
    area=math.pi*num*num
    print("area of ciralce=",area)
elif ch==3:
    num1=float(input("enter length="))
    num2=float(input("enter width="))
    print("area of rectangle=",num1*num2)
else:
    print("enter valid choice!")