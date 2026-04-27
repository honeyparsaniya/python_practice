n=int(input("enter size of set="))
my_set=set()

for i in range(n):
    val=int(input("enter value="))
    my_set.add(val)
print("your set=",my_set)
print(type(my_set))