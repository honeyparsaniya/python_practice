print("kwargs_example")
def student_info(**data):
    for key, value in data.items():
        print(key, ":", value)

name = input("Enter name: ")
age = input("Enter age: ")
city = input("Enter city: ")

student_info(name=name, age=age, city=city)