print("fibonaci serice")

num=int(input("enter a last number="))

a=0;
b=1;
i=1;

while i<=num:

    print(a)
    c=a+b;
    a=b;
    b=c;
    i=i+1;