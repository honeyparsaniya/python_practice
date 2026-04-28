d = {}
n = int(input("Enter number of elements: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

key = input("Enter key: ")
value = input("Enter default value: ")

result = d.setdefault(key, value)

print("Returned value:", result)
print("Dictionary:", d)