lst = [1, 2, 3, 4, 5]

n = int(input("Enter rotation: "))

for i in range(n):
    first = lst[0]
    for j in range(len(lst) - 1):
        lst[j] = lst[j + 1]
        print("-----------------------------")
        print(f"{lst[j]}----- {lst[j+1]}")
        print("-----------------------------")

    lst[-1] = first

    print("==================================")
    print(lst[-1])
    print("==================================")

print("Rotated List:", lst)