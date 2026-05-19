import cartmodule

while True:

    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. Show Cart")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        item = input("Enter Item: ")
        cartmodule.add_item(item)

    elif choice == 2:

        item = input("Enter Item to Remove: ")
        cartmodule.remove_item(item)

    elif choice == 3:

        print("Cart Items =", cartmodule.show_cart())

    elif choice == 4:
        break

    else:
        print("Invalid Choice")