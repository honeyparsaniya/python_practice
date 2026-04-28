n=int(input("enter size of dictionary="))

d={}

for i in range(n):
    key=input("enter key=")
    value=input("enter value=")
    print()
    d[key]=value

print("your dictionary=",d)
print("copy first dictionary")

d2=d.copy()
print("your second dictionary=",d2)