print("factorial of number")

def fact_num(n):
    fact=1
    for i in range(1,n+1):
        fact= fact*i
    return fact
    
num=int(input("enter number="))
result=fact_num(num) 
print("factorial of given number=",result)