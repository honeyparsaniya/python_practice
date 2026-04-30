n=int(input("enter total number of student="))

student=[]

for i in range(n):
    name=input("enter student name=")
    mark=int(input("enter mark="))
    student.append((name,mark))
print("===total student list===")
print(student)
print()

#filter student ,mark above 40
pass_student=list(filter(lambda x:x[1]>=40,student))
print("===pass student list===")
print(pass_student)
print()

#add 5 bonus mark
b_student=list(map(lambda x:(x[0],x[1]+1),pass_student))
print("===pass student after adding bonus mark")
print(b_student)
print()

#sort student using high to low(desending order)
sort_student=sorted(b_student,key=lambda x: x[1],reverse=True)

print("final result")

for i in sort_student:
    print(i)
