class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("===student Detail===")
        print("Name:", self.name)
        print("Marks:", self.marks)

name = input("Enter name: ")
marks = input("Enter marks: ")

s1 = Student(name, marks)
s1.display()