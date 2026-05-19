import studentmodule

m1 = int(input("Enter Marks 1: "))
m2 = int(input("Enter Marks 2: "))
m3 = int(input("Enter Marks 3: "))

tot = studentmodule.total(m1, m2, m3)

per = studentmodule.percentage(tot)

print("Total =", tot)
print("Percentage =", per)
print("Result =", studentmodule.result(per))