import math

print("1. Square Root")
print("2. Power")
print("3. Factorial")
print("4. Ceil Value")
print("5. Floor Value")
print("6. Area of Circle")
print("7. GCD")
print("8. Absolute Value")
print("9. Remove Decimal")
print("10. Integer Square Root")
print("11. Sine Value")
print("12. Cosine Value")
print("13. Tangent Value")
print("14. Log Value")
print("15. Degree to Radian")
print("16. Radian to Degree")
print("17. Exponential Value")

ch=int(input("Enter choice="))

if ch==1:
    num=float(input("enter number="))
    print("squre root of number=",math.sqrt(num))
elif ch==2:
    num=float(input("enter number="))
    power=float(input("enter power="))
    print("answer=",math.pow(num,power))
elif ch==3:
    num=int(input("enter a number="))
    print("factorial=",math.factorial(num))
elif ch==4:
    num=float(input("enter a number="))
    print("answer=",math.ceil(num))
elif ch==5:
    num=float(input("enter a number="))
    print("answer=",math.floor(num))

elif ch == 6:
    radius = float(input("Enter radius: "))
    area = math.pi * radius * radius
    print("Area of Circle =", area)

elif ch == 7:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("GCD =", math.gcd(a, b))

elif ch == 8:
    num = float(input("Enter number: "))
    print("Absolute Value =", math.fabs(num))

elif ch == 9:
    num = float(input("Enter decimal number: "))
    print("Truncated Value =", math.trunc(num))

elif ch == 10:
    num = int(input("Enter number: "))
    print("Integer Square Root =", math.isqrt(num))

elif ch == 11:
    angle = int(input("Enter angle: "))
    print("Sine Value =", math.sin(angle))

elif ch == 12:
    angle = int(input("Enter angle: "))
    print("Cosine Value =", math.cos(angle))

elif ch == 13:
    angle = int(input("Enter angle: "))
    print("Tangent Value =", math.tan(angle))

elif ch == 14:
    num = int(input("Enter number: "))
    print("Log Value =", math.log(num))

elif ch == 15:
    degree = int(input("Enter degree: "))
    print("Radian =", math.radians(degree))

elif ch == 16:
    radian = float(input("Enter radian: "))
    print("Degree =", math.degrees(radian))

elif ch == 17:
    num = int(input("Enter number: "))
    print("Exponential Value =", math.exp(num))

else:
    print("Invalid Choice")