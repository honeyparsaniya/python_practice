def my_decoretors(func):
    def wrapper():
        print("before function call")
        func()
        print("after function call")
    return wrapper
    
@my_decoretors
def say_hello():
    print("hello honey")

say_hello()
