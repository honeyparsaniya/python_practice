print("serch elment in list and remove that element")

n=int(input("enter size of list="))
list=[]

for i in range(n):
    val=int(input("enter value in string="))
    list.append(val)

num=int(input("enter value want to remove="))

found=False
for i in list:
    if num==i:
        list.remove(i)
        found=True

if found:
    print("element found and removed")
    print(list)
else:
    print("element not found")

