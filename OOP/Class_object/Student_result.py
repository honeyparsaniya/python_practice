class student:
    def show(self,name,mark):
        print("---student detail---")
        print("name=",name)
        if mark>70:
            print("pass with grade A")
        elif mark>50:
            print("pass with grade B")
        elif mark>35:
            print("pass with grade C")
        else:
            print("Fail!")

name=input("enter name=")
mark=int(input("enter your result="))

s1=student()
s1.show(name,mark)