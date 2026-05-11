class Student:

    def __init__(self):
        self.name=input("enter student name=")
        self.result=float(input("enter student result="))

    def display(self):
        print("====student detail====")
        print("Name=",self.name)
        print("Result=",self.result)

s1=Student()

#access outside class
s1.name=input("enter new name=")

s1.display()