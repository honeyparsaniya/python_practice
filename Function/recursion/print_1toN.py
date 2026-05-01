def print_numbers(n):
    # Base condition
    if n == 0:
        return
    else:
        print_numbers(n - 1)
        print(n)


num = int(input("Enter a number: "))

if num <= 0:
    print("Enter a positive number.")
else:
    print("Numbers from 1 to", num, "are:")
    print_numbers(num)