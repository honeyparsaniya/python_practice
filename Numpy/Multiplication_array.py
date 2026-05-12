import numpy as np

n=int(input("enter size of array="))

numbers=[]

for i in range(n):
    val=int(input("Enter value="))
    numbers.append(val)

arr=np.array(numbers)

mul_value=int(input("enter value for multiply="))

print("\noriginal array=",arr)
print("array after multiply=",arr*mul_value)