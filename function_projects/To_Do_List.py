#to do list 
tasks=[]

def add_task():
    task=input("enter task=")
    tasks.append(task)
    print("task added successfully.")

def view_task():
    if not tasks:
        print("no task in the list")
        return

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task():
    task=input("enter task want to delete=")
    if task in tasks:
        tasks.remove(task)
        print("task successfully deleted.")
    else:
        print("task not found!")

while True:
    print("===to do list===")
    print("1.add task")
    print("2.view task")
    print("3.delete task")
    print("4.exit")

    ch=int(input("enter your choice=(1-4)="))

    if ch==1:
        add_task()
    elif ch==2:
        view_task()
    elif ch==3:
        delete_task()
    elif ch==4:
        break
    else:
        print("enter valid choice!")
       
