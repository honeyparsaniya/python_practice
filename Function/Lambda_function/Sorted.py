n=int(input("enter size="))
numbers=[]

for i in range (n):
    val=int(input("enter number="))
    numbers.append(val)
    
#sorting in assending order

sort=sorted(numbers)
print("in asending order=",sort)