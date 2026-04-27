n=int(input("enter size of tupel="))
list=[]

for i in range(n):
    val=int(input("enter value="))
    list.append(val)

tpl=tuple(list)
print("your tuple =",tpl)

x=int(input("enter value to check occurence="))
count=0;

for i in tpl:
    if i==x:
        count=count+1

print("-----------")
print(f"{x} is arrive {count} times in tuple")
print("-----------")
         
