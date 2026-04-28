n=int(input("enter size of dictionary="))

d={}

for i in range(n):
    key=input("enter key=")
    value=input("enter value=")
    print()
    d[key]=value
print("your dictionary=",d)

print("add new element in dictionary")

new_key=input("enter new key=")
new_value=input("enter new value=")
d[new_key]=new_value
print()
print("new dictionary=",d)
