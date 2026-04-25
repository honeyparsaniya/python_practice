print("sum of even number")

num=int(input("enter a last number="))

total=0;

for i in range(0,num+1):
    if i%2==0:
        #print(f"{i} +")
        total=total+i;
print("sum=",total)