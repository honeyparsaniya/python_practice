n=int(input("enter size="))

numbers=[]

for i in range(n):
    val=int(input("enter a number="))
    numbers.append(val)

squre = list(map(lambda x : x*x,numbers))

print("squres=",squre)