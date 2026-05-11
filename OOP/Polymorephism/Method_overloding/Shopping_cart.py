class Shopping:

    def checkout(self, mobile=0, earbuds=0, charger=0):

        total = mobile + earbuds + charger

        print("Cart Total =", total)


s1 = Shopping()

print("PRODUCTS")
print("1. Mobile = 15000")
print("2. Earbuds = 2000")
print("3. Charger = 800")

print("1. Buy Mobile")
print("2. Buy Mobile + Earbuds")
print("3. Buy Mobile + Earbuds + Charger")

choice = int(input("Enter choice: "))

if choice == 1:
    s1.checkout(15000)

elif choice == 2:
    s1.checkout(15000, 2000)

elif choice == 3:
    s1.checkout(15000, 2000, 800)

else:
    print("Invalid Choice")