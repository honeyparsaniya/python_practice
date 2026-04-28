n=int(input("enter size of dictionary="))

d={}

for i in range(n):
    key=input("enter key=")
    value=input("enter value=")
    d[key]=value

print("your dictionary=",d)