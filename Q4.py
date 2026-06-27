#Q.4) 
# Class to store student information
class Student:
    # Constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []
    # Method to add marks
    def add_mark(self, mark):
        try:
            mark = float(mark)
            if mark < 0 or mark > 100:
                raise ValueError("Marks should be between 0 and 100.")
            self.marks_list.append(mark)
        except ValueError as e:
            print("Invalid Input:", e)
    # Method to calculate average
    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)
    # Method to display student details
    def display_info(self):
        print("\n----- Student Details -----")
        print("Name :", self.name)
        print("Roll No :", self.roll_no)
        print("Marks :", self.marks_list)
        print("Average :", round(self.get_average(), 2))
# Main Program
name = input("Enter student name: ")
roll = input("Enter roll number: ")
student = Student(name, roll)
print("\nEnter 5 marks:")
for i in range(5):
    mark = input(f"Mark {i + 1}: ")
    student.add_mark(mark)
student.display_info()
