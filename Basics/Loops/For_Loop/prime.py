print("check number is prime or not")
num=int(input("enter a number="))

if num<=1:
    print("number is not valid")
else:
    is_prime=True

    for i in range(2,num//2+1):
        if num%i==0:
            is_prime=False
            break
        if is_prime:
            print(" given number is prime")
        else:
            print("given number is not prime")