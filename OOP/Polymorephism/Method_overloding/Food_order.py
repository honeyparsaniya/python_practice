class FoodOrder:

    def bill(self, pizza=0, burger=0, coke=0):

        total = pizza + burger + coke

        print("Final Bill =", total)


f1 = FoodOrder()

print("MENU")
print("Pizza = 250")
print("Burger = 120")
print("Coke = 60")

print("1. Pizza")
print("2. Pizza + Burger")
print("3. Pizza + Burger + Coke")

choice = int(input("Enter choice: "))

if choice == 1:
    f1.bill(250)

elif choice == 2:
    f1.bill(250, 120)

elif choice == 3:
    f1.bill(250, 120, 60)

else:
    print("Invalid Choice")