numbers = []

n = int(input("How many numbers: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", even_numbers)