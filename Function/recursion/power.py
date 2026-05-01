def power(base, exponent):
    # Base condition
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

base = int(input("Enter base number: "))
exp = int(input("Enter exponent: "))

result = power(base, exp)
print(base, "raised to the power", exp, "is:", result)