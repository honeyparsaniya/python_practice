print("check number is prime or not")
def check_prime(n):
    for i in range(2,n):
        if n%i==0:
            return "number is  not prime"
        else:
            return  "number is prime"
        
num=int(input("enter number ="))
print(check_prime(num))