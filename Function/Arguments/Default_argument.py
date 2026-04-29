print("default argument.")
def data(name="honey"):
    print("your name is ",name)

name=input("enter your name=")
if name=="":
    data ()
else:
    data (name)