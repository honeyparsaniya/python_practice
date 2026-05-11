list=[]

num=int(input("enter length of list="))

for i in range(num):
    val=int(input("enter value="))
    list.append(val)

serch=int(input("enter value for serch="))

for i in list:

    if i==serch:

        print("value find")