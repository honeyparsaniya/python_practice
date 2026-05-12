import numpy as np

n=int(input("Enter size of array="))

numbers=[]

for i in range(n):
    val=int(input("Enter value="))
    numbers.append(val)

arr=np.array(numbers)


print("NumPy array=",arr)