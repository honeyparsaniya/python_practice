n=int(input("enter size of set="))
my_set=set()

for i in range(n):
    val=int(input("enter value="))
    my_set.add(val)
print("your set=",my_set)

if len(my_set) > 0:
    removed = my_set.pop()
    print("Removed Element:", removed)
else:
    print("Set is empty")

print("Updated Set:", my_set)