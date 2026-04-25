#check positive/negative/zero

num=int(input("enter number="))

print("you enter=",num)

if num>0:
    print(f"{num} is positive.")
elif num<0:
    print(f"{num} is negative. ")
else:
    print(f"{num} is zero")