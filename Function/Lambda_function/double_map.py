
numbers = []

n = int(input("How many numbers you want to enter: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

# lambda function
double_func = lambda x: x * 2

result = []

for i in range(len(numbers)):
    value = numbers[i]
    doubled = double_func(value)
    result.append(doubled)

print("Doubled numbers:", result)