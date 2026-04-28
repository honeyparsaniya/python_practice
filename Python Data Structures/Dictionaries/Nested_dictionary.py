students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    sid = input("Enter student ID: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    # nested dictionary
    students[sid] = {
        "name": name,
        "age": age,
        "course": course
    }

print("\nStudent Records:")

for sid, info in students.items():
    print("\nID:", sid)
    print("Name:", info["name"])
    print("Age:", info["age"])
    print("Course:", info["course"])