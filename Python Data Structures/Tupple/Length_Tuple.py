n=int(input("enter size of tuple="))

list=[]
for i in range(n):
    val=int(input("enter value in tuple="))
    list.append(val)

tpl=tuple(list)
print()
print("tuple is =",tpl)


count=0;
for i in tpl:
    count=count+1

print("------------------")
print("length of tuple is ",count)
print("------------------")
