print("find armstrong")

num=int(input("enter a number="))
temp=num
count=0;
t=num
while t>0:

    count=count+1;
    t=t//10;

sum=0;

while num>0:

    digit=num%10
    sum=sum+digit**count
    num=num//10

if sum==temp:
    print("given number is armstrong number")
else:
    print("given number is not armstrong")
    