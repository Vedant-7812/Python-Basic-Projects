#Q.5)
# Function to manage student database
def student_database():
    students = {}
    while True:
        print("\n===== Student Database Menu =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                roll = int(input("Enter Roll Number: "))
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")
                # Add student using update()
                students.update({
                    roll: {
                        "Name": name,
                        "Age": age,
                        "City": city
                    }
                })
                print("Student added successfully.")
            except ValueError:
                print("Invalid input! Please enter correct data.")
        elif choice == "2":
            try:
                roll = int(input("Enter Roll Number to Search: "))
                student = students.get(roll)
                if student:
                    print("\nStudent Found")
                    print("Name :", student["Name"])
                    print("Age  :", student["Age"])
                    print("City :", student["City"])
                else:
                    print("Student not found.")
            except ValueError:
                print("Roll Number must be numeric.")
        elif choice == "3":
            if not students:
                print("No student records available.")
            else:
                print("\n----- Student Records -----")
                for roll, info in students.items():
                    print(f"\nRoll Number : {roll}")
                    print("Name :", info["Name"])
                    print("Age  :", info["Age"])
                    print("City :", info["City"])
        elif choice == "4":
            print("Exiting Student Database...")
            break
        else:
            print("Invalid choice! Please select between 1 and 4.")
# Main Program
student_database()
