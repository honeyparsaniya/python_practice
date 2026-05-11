n=int(input("enter total subject="))
list=[]

for i in range(n):

    val=int(input("enter mark="))
    list.append(val)

total=0
for i in list:
    total=total+i

avg=total/n

print("total number of subject=",n)
print("mark=",list)
print("total=",total)
print("result=",avg)