class employee:

    def __init__(self,emp_id,emp_name,emp_sal,emp_dep):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_sal=emp_sal
        self.emp_dep=emp_dep

    def __str__(self):
        
        return(
            f"\nEmployee ID             :{self.emp_id}"
            f"\nEmployee Name           :{self.emp_name}"
            f"\nEmployee Salary         :{self.emp_sal}"
            f"\nEmployee department     :{self.emp_dep}"
        )
    
id=int(input("Enter employee id="))
name=input("Enter employee name=")
dep=input("Enter employee Department=")
salary=float(input("Enter employee salary="))

e1=employee(id,name,dep,salary)

print("\n-Employee Details")
print(e1)