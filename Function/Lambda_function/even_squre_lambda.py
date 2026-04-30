n=int(input("enter size="))
numbers=[]

for i in range(n):
    val=int(input("enter number="))
    numbers.append(val)

#keep even value using filter
even=list(filter(lambda x: x % 2==0,numbers))

#squre of even value
squre=list(filter(lambda x: x*x ,even))

print()
print("even number=",even)
print()
print("squre of even value=",squre)