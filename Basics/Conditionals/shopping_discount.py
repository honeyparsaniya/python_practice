membership=input("enter membership type(Premium/Regular/None)=")
amount=float(input("enter purchase amount="))

if membership == "Premium":
    discount = 0.20
    print("Applying 20% Premium discount.")
elif membership == "Regular":
    if amount > 500:
        discount = 0.10
        print("Applying 10% Regular (High Value) discount.")
    else:
        discount = 0.05
        print("Applying 5% Regular discount.")
else:
    discount = 0
    print("No discount applied.")

final_price = amount - (amount * discount)
print(f"Final Price: {final_price=:.2f}")