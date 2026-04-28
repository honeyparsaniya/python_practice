n=int(input("enter size of dictionary="))

d={}

for i in range(n):
    key=input("enter key=")
    value=input("enter value=")
    d[key]=value
print("your dictionary=",d)

print("--------------------------------------------------------------------------------------")

key=input("enter key to update=")

if key in d:
    new_value=input("enter value=")
    d[key]=new_value
    print("your updated dictionary=",d)
else:
    print("key not found")