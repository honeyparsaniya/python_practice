print("sepret even and odd value in list")
n=int(input("enter sixe of  list="))
list=[]

for i in range(n):
    val=int(input("enter value in list="))
    list.append(val)
print()
print("original list")
print(list)
print()

even=[]
odd=[]

for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print()
print("even value in list")
print(even)
print()
print("odd value in string")
print(odd)
