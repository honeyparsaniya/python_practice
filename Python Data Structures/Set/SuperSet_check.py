# Program to check superset

set1 = set()
set2 = set()

n1 = int(input("Enter elements for Set 1: "))
for i in range(n1):
    value = int(input("Enter element: "))
    set1.add(value)

n2 = int(input("Enter elements for Set 2: "))
for i in range(n2):
    value = int(input("Enter element: "))
    set2.add(value)

if set1.issuperset(set2):
    print("Set1 is superset of Set2")
else:
    print("Set1 is NOT superset of Set2")