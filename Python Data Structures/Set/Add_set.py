print("take value for set")
n=int(input("enter size of set="))

my_set=set()

for i in range(n):
    val=int(input("enter value="))
    my_set.add(val)
print("your set=",my_set)
print()
print("take new value for add in set")
print()

new=int(input("enter new value wnat to add in set="))

my_set.add(new)

print()
print("updated set=",my_set)