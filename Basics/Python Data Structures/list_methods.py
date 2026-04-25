n=int(input("enter size of list="))
list=[]

for i in range(n):
    val=input("enter valuse in list=")
    list.append(val)

print("original list")
print(list)

#append
list.append("40")
print("after append=",list)

#extend
list.extend([10,20])
print("after extend=",list)

#insert
list.insert(3,'honey')
print("after add on 3rd index=",list)

#remove
list.remove('honey')
print("remove honey from list=",list)

#pop
list.pop()
print("pop by default=",list)

#sort
#list.sort()
#print("list after sort=",list)


#reverse
list.reverse()
print("list after reverse=",list)

#clear
list.clear()
print("list after clear=",list)