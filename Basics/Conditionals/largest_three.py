#find maximum value from three number

num1=int(input("enter first number="))
num2=int(input("enter second number="))
num3=int(input("enter third number="))

print(f"you enter {num1},{num2} and {num3}")

if num1>num2 and num2>num3:
    print("first number is maximum")
elif num2>num3:
    print("second number is maximum")
else:
    print("third number is maximum")
         