n=int(input("enter size of tuple="))

list=[]
for i in range(n):
    val=int(input("enter value in tuple="))
    list.append(val)

tpl=tuple(list)
print()
print("tuple is =",tpl)
