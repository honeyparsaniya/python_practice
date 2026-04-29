def log_system(func):
    def wrapper():
        username=input("enter uaer name=")
        password=input("enter password=")

        if username=="honey" and password=="honey_1234":
            print("login successfull")
            func()

        else:
                print("login failed")
    return wrapper

@log_system
def deshbord():
     print("welcome to deshbord")

deshbord()