print("second largest element in list")
n=int(input("enter a sixe of list="))
list=[]

for i in range(n):
    val=int(input("enter number in list="))
    list.append(val)
print("your list=",list)

largest=list[0]
second=list[0]

for i in list:
    if i>largest:
        second=largest
        largest=i
    elif i> second and i!=largest:
        second=i
print("second largest elemment in list is ",second)
