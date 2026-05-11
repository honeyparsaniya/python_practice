#perent class
class Student:
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3

#child class
class Result(Student):
    def display(self):
        total=self.m1+self.m2+self.m3
        per=total/3
        print("NAME=",self.name)
        print("TOTAL=",total)
        print("RESULT=",per)

#user input
name=input("enter your name=")
m1=int(input("enter mark(Subject-1)="))
m2=int(input("enter mark(Subject-2)="))
m3=int(input("enter mark(Subject-3)="))

#creat object 
r1=Result(name,m1,m2,m3)
r1.display()