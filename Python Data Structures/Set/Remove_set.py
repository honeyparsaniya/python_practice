n=int(input("enter size of set="))
my_set=set()

for i in range(n):
    val=int(input("enter value="))
    my_set.add(val)
print("your set=",my_set)

print("--------------------")
print("remove item from set")
print("---------------------")

m=int(input("enter element want to remove="))


if m in my_set:
        my_set.remove(m)
        print("value remove successfully")
else:
        print("value not found")

print("updated set=",my_set)