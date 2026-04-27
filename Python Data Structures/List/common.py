print("find common item from two list")
print()
n=int(input("enter size of both list="))
list1=[]
list2=[]

for i in range(n):
    val1=int(input("enter value in first list="))
    list1.append(val1)
print()
for i in range(n):
    val2=int(input("enter value in second list="))
    list2.append(val2)

print()
print("1st list")
print(list1)
print()
print("second list")
print(list2)

common=[]

for i in list1:
    if i in list2 and i not in common:
        common.append(i)

print()
print("common item=",common)