class Result:

    def marks(self, sub1, sub2=0, sub3=0):

        total = sub1 + sub2 + sub3

        if sub2 == 0 and sub3 == 0:
            avg = total / 1

        elif sub3 == 0:
            avg = total / 2

        else:
            avg = total / 3

        print("Total =", total)
        print("Average =", avg)


r1 = Result()

print("1. One Subject")
print("2. Two Subjects")
print("3. Three Subjects")

choice = int(input("Enter choice: "))

if choice == 1:

    s1 = int(input("Enter Subject 1 Marks: "))
    r1.marks(s1)

elif choice == 2:

    s1 = int(input("Enter Subject 1 Marks: "))
    s2 = int(input("Enter Subject 2 Marks: "))
    r1.marks(s1, s2)

elif choice == 3:

    s1 = int(input("Enter Subject 1 Marks: "))
    s2 = int(input("Enter Subject 2 Marks: "))
    s3 = int(input("Enter Subject 3 Marks: "))
    r1.marks(s1, s2, s3)

else:
    print("Invalid Choice")