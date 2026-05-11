class University:

    def __init__(self, uni_name):
        self.uni_name = uni_name

    def show_university(self):
        print("\nUniversity Name:", self.uni_name)

    class Department:

        def __init__(self, dept_name, total_students):
            self.dept_name = dept_name
            self.total_students = total_students

        def department_grade(self):
            if self.total_students > 500:
                print("Department Grade: A")
            else:
                print("Department Grade: B")

        def show_department(self):
            print("Department Name:", self.dept_name)
            print("Total Students:", self.total_students)


# User Input
uni_name = input("Enter University Name: ")
dept_name = input("Enter Department Name: ")
students = int(input("Enter Total Students: "))

u1 = University(uni_name)
d1 = University.Department(dept_name, students)

u1.show_university()
d1.show_department()
d1.department_grade()