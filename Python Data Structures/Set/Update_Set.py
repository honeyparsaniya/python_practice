n=int(input("enter size of set="))
my_set=set()

for i in range(n):
    val=int(input("enter value="))
    my_set.add(val)
print("your set=",my_set)
print()

print("update set")

m=int(input("enter number of element that you want to add ="))
list=[]

for i in range(m):
    val2=int(input("enter value="))
    list.append(val2)

my_set.update(list)

print("updated set =",my_set)