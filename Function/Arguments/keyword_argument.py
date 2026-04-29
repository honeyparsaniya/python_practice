print("keyword_argument.")
def data(n,a):
    print("name=",n)
    print("age=",a)

name=input(input("enter your name="))
age=int(input("enter age="))

data(a=age,n=name)