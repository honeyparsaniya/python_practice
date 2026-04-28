n=int(input("enter size of dictionary="))

d={}

for i in range(n):
    key=input("enter key=")
    value=input("enter value=")
    d[key]=value

print("your dictionary=",d)
print("============================================================================")

if len(d)>0:
    d.popitem()
    print("after pop iteam=",d)
else:
    print("dictionary is empty")