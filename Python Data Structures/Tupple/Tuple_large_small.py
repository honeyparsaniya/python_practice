n = int(input("Enter number of elements: "))

lst = []
for i in range(n):
    val = int(input("Enter value: "))
    lst.append(val)

t = tuple(lst)

largest = t[0]
smallest = t[0]

for i in t:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest:", largest)
print("Smallest:", smallest)