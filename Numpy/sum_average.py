import numpy as np

n=int(input("enter size of array="))
numbers=[]

for i in range(n):
    val=int(input("enter value="))
    numbers.append(val)

arr=np.array(numbers)

print("\nArray=",arr)
print("Sum=",np.sum(arr))
print("Avarage=",np.mean(arr))