n = int(input("Enter number of keys: "))
keys = []

for i in range(n):
    key = input("Enter key: ")
    keys.append(key)
    
value = input("Enter common value: ")

d = dict.fromkeys(keys, value)

print("Dictionary:", d)