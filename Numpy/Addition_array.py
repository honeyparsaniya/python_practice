import numpy as np

n=int(input("enter size of array="))

numbers=[]

for i in range(n):
    val=int(input("Enter value="))
    numbers.append(val)

arr=np.array(numbers)

add_value=int(input("enter value to add="))

print("original array=",arr)
print("after addition=",arr+add_value)