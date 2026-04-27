n = int(input("Enter number of elements: "))

lst = []
for i in range(n):
    val = int(input("Enter value: "))
    lst.append(val)

t = tuple(lst)

max_val = t[0]

for i in t:
    if i > max_val:
        max_val = i

print("Maximum value:", max_val)