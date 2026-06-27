#Q.3)
# Function to manage subject marks
def manage_marks():
    marks = []
    print("Enter marks for 5 subjects:")
    while len(marks) < 5:
        try:
            mark = float(input(f"Subject {len(marks) + 1}: "))
            if mark < 0 or mark > 100:
                print("Marks should be between 0 and 100.")
                continue
            marks.append(mark)
        except ValueError:
            print("Invalid input! Please enter numeric marks.")
    # Calculate results
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    # Sort in descending order
    sorted_marks = sorted(marks, reverse=True)
    # Display results
    print("\n----- Result -----")
    print("Marks List:", marks)
    print("Average Marks:", round(average, 2))
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)
    print("Marks in Descending Order:", sorted_marks)
# Main Program
manage_marks()
