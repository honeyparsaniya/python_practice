print("check given number is palidrom or not")

num=int(input("enter a number="))

temp=num;
rev=0;

while num>0:

    digit=num%10;
    rev=rev*10+digit;
    num=num//10;
if temp==rev:
    print("given number is palidrom")
else:
    print("given number is not palidrom")