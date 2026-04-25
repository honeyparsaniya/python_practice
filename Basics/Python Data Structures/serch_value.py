print("serch element value from string")

n=int(input("enter size of list="))
list=[]

for i in range(n):
    val=int(input("enter value in list="))
    list.append(val)

print()
print("original list")
print(list)

num=int(input("enter value that you want to find="))

found=False

for i in list:
    if i ==num:
        found=True
        break

if found:
    print("number is found in list")
else:
    print("number not found in list")