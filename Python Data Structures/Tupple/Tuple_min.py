n = int(input("Enter number of elements: "))

lst = []
for i in range(n):
    val = int(input("Enter value: "))
    lst.append(val)

t = tuple(lst)

min_val = t[0]

for i in t:
    if i < min_val:
        min_val = i

print("Minimum value:", min_val)