n=int(input("enter size="))
number=[]

for i in range(n):
    val=int(input("enter value="))
    number.append(val)

print("===choose sorting type===")
print("1.assending order")
print("2.desending order")

choice=int(input("enter choice="))

if choice==1:
    a_sort=sorted(number)
    print("asending ordr=",a_sort)
elif choice==2:
    d_sort=sorted(number,reverse=True)
    print("decending order=",d_sort)
else:
    print("invalid choice")