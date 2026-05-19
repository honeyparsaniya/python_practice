import mymodule

password = input("Enter Password: ")

if mymodule.is_strong_password(password):
    print("Strong Password")

else:
    print("Weak Password")