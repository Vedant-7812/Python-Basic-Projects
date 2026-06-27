#Q.8)
# Class to store employee details
class Employee:
    # Constructor
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.details = (department, salary)   # Tuple
    # Method to display employee details
    def show_details(self):
        print("\nEmployee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Department  :", self.details[0])
        print("Salary      :", self.details[1])
# Dictionary to store Employee objects
employees = {}
# Add 3 employees
for i in range(3):
    print(f"\nEnter details of Employee {i + 1}")
    emp_id = input("Employee ID: ")
    name = input("Name: ")
    department = input("Department: ")
    while True:
        try:
            salary = float(input("Salary: "))
            break
        except ValueError:
            print("Invalid salary! Please enter a numeric value.")
    # Create Employee object
    emp = Employee(emp_id, name, department, salary)
    # Store object in dictionary
    employees[emp_id] = emp
# Display all employee details
print("\n===== Employee Details =====")
for emp in employees.values():
    emp.show_details()
