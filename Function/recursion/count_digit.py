def count_digits(n):
    # Base condition
    if n == 0:
        return 0
    else:
        return 1 + count_digits(n // 10)

num = int(input("Enter a number: "))

if num == 0:
    print("Number of digits: 1")
else:
    digits = count_digits(abs(num))
    print("Number of digits:", digits)