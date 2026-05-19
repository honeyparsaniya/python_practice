import mymodule

email = input("Enter Email: ")

if mymodule.is_valid_email(email):
    print("Valid Email")

else:
    print("Invalid Email")