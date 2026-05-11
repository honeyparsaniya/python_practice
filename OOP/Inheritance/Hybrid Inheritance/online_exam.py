class Student:

    def student_info(self):

        self.name = input("Enter Student Name: ")
        self.roll = int(input("Enter Roll Number: "))


class Theory(Student):

    def theory_marks(self):

        self.python = int(input("Enter Python Marks: "))
        self.java = int(input("Enter Java Marks: "))


class Practical(Student):

    def practical_marks(self):

        self.practical = int(input("Enter Practical Marks: "))
        self.viva = int(input("Enter Viva Marks: "))


class Result(Theory, Practical):

    def final_result(self):

        total = self.python + self.java + self.practical + self.viva

        percentage = total / 4

        if percentage >= 75:
            grade = "A"

        elif percentage >= 60:
            grade = "B"

        elif percentage >= 35:
            grade = "C"

        else:
            grade = "Fail"

        print("\n===== Final Result =====")

        print("Student Name :", self.name)
        print("Roll Number  :", self.roll)

        print("Total Marks  :", total)
        print("Percentage   :", percentage)
        print("Grade        :", grade)


r = Result()

r.student_info()
r.theory_marks()
r.practical_marks()
r.final_result()