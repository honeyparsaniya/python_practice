import random

product = input("Enter product name: ")
price = float(input("Enter product price: "))

discount=random.random()*50

discount_amount=(price*discount)/100
final_price = price - discount_amount

print("\nProduct:", product)
print("Original Price:", price)

print("Discount:", round(discount, 2), "%")

print("Final Price:", round(final_price, 2))