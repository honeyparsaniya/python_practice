#perent clsss 1

class get_detail:

    def detail(self):

        self.name=input("enter name=")
        self.no=int(input("enter enrollment number="))
        self.div=input("enter your division=")

#perent class 2
class get_result:

    def result(self):
         self.total=int(input("enter total mark="))
         self.attendence=int(input("enter your attendance="))

# child class

class view_data(get_detail,get_result):

    def display(self):

        print("Student Name=",self.name)
        print("Student Enrollment number=",self.no)
        print("student Division=",self.div)
        if self.total>40 and self.attendence>=75:
            print("PASS in exam")
        else:
            print("FAIL IN EXAM")

print("===Student Result system===")
v=view_data()
v.detail()
v.result()
v.display()
