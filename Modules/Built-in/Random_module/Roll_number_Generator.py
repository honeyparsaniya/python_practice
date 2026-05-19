import random

start = int(input("Enter starting roll number: "))
end = int(input("Enter ending roll number: "))

roll = random.randrange(start, end)

print("Selected Roll Number is:", roll)