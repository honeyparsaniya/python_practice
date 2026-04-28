n=int(input("enter size of dictionary="))

d={}

for i in range(n):
    key=input("enter key=")
    value=input("enter value=")
    d[key]=value
    print()
print("your dictionary=",d)

print("---------------------------------------------------------")

key=input("enter key to delete=")

if key in d:
    del d[key]
    print("dictionary after delete=",d)
else:
    print("key value not found")