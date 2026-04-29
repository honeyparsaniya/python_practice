print("args argument example")
def sum_num(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("total=",sum)
print()
list=[]

n=int(input("enter size="))

for i in range(n):
    value=int(input("enter value="))
    list.append(value)

sum_num(*list)