n1=int(input("enter size of set 1="))
my_set1=set()

for i in range(n1):
    val1=int(input("enter value="))
    my_set1.add(val1)


print("-------------------------------------")
n2=int(input("enter size of set 2="))
my_set2=set()

for i in range(n2):
    val=int(input("enter value="))
    my_set2.add(val)

print("--------------------------------------")

result=my_set1.difference(my_set2)

print("your set 1=",my_set1)
   
print("your set=",my_set2)

print("union of set=",result)