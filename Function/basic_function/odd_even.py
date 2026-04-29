print("chech number is even or odd")
def check_num(n):
    if n%2==0:
        return "number is even"
    else:
        return "number is odd"
num=int(input("enter number="))

message=check_num(num)
print(message)