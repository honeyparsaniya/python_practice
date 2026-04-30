n=int(input("enter total number of product="))
product=[]

for i in range(n):
    name=input("enter product name=")
    price=int(input("enter price of product="))

    product.append((name,price))
print()
print(product)
print()
#keep only value above 500
expansive=list(filter(lambda x: x[1]>500,product))

#apply discount on that
discount=list(map(lambda x:(x[0],x[1]*0.9),expansive))

#now sort product using price
sort=list(sorted(discount,key=lambda x:x[1]))

print("final product after sorting and discount")

print(sort)
