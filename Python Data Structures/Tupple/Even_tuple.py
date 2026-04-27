n = int(input("Enter number of elements: "))

lst = []
for i in range(n):
    val = int(input("Enter value: "))
    lst.append(val)

t = tuple(lst)

print("Even numbers:")

for i in t:
    if i % 2 == 0:
        print(i)