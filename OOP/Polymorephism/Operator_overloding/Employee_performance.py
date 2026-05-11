class Employee:

    def __init__(self,name,sales):
        self.name=name
        self.sales=sales

    def __gt__(self, other):
        if self.sales>other.sales:
            return self.name
        else:
            return other.name
        
name1=input("enter first employee name=")
salse1=int(input("enter second employee sales="))

name2=input("enter second employee name=")
sales2=int(input("enter second employee sales="))

e1=Employee(name1,sales2)
e2=Employee(name2,sales2)

print("best performare=",e1>e2)