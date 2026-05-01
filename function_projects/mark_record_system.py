#mark recoed system
marks={}

def add_mark():
    name=input("enter student name=")
    mark=int(input("enter mark="))
    marks[name]=mark
    print("data added sucessflly")

def view_data():
    if not marks:
        print("storage is empty")
    for name,mark in marks.items():
        print(f"{name}={mark}")

def find_data():
    name=input("enter name=")
    if name in marks:
        print(f"{name} mark is {marks[name]}")
    else:
        print("student not found!")

while True:
    print("===student_mark_management===")
    print("1.add mark")
    print("2.view mark")
    print("3.find mark")
    print("4.exit")
    choice=int(input("enter choice(1-4)="))

    if choice==1:
        add_mark()
    elif choice==2:
        view_data()
    elif choice==3:
        find_data()
    elif choice==4:
        break
    else:
        print("enter valid choice!")