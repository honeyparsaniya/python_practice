num=int(input("enter a number="))

count=0;

for i in range(0,num+1):
    if i%2!=0:
        count=count+1;

print("total odd count=",count)