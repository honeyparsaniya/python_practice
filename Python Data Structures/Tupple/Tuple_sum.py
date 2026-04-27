n = int(input("Enter number of elements: "))

lst = []
for i in range(n):
    val = int(input("Enter value: "))
    lst.append(val)

t = tuple(lst)

total = 0

for i in t:
    total += i

print("Sum:", total)