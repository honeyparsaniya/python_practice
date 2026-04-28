n = int(input("Enter number of elements: "))

s = set()

for i in range(n):
    val = input("Enter value: ")
    s.add(val)

fs = frozenset(s)

print("Frozenset =", fs)

x = input("Enter value to check: ")

if x in fs:
    print("Value exists")
else:
    print("Value not found")