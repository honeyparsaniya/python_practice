def sum_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_n(n - 1)

num = int(input("Enter a positive number: "))

if num <= 0:
    print("Enter a number greater than 0.")
else:
    print("Sum of first", num, "numbers is:", sum_n(num))