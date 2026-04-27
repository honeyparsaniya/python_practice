n=int(input("enter size of tupel="))
list=[]

for i in range(n):
    val=int(input("enter value="))
    list.append(val)

tpl=tuple(list)
print("your tuple =",tpl)

x=int(input("enter value to check occurence="))
ind=-1
i=0


for val in tpl:
    if val==x:
        ind=i
        break
    i=i+1

if ind ==-1:
    print("value not found")
else:
    print("value found at index ",i)