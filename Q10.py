#Q.10)
# Smart Calculator & Data Manager
import math
import random
# Dictionary to store history
history = {}
count = 1
# Function for Basic Arithmetic
def basic_arithmetic():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("\nChoose Operation")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = input("Enter your choice: ")
        if choice == "1":
            result = num1 + num2
            operation = f"{num1} + {num2}"
        elif choice == "2":
            result = num1 - num2
            operation = f"{num1} - {num2}"
        elif choice == "3":
            result = num1 * num2
            operation = f"{num1} * {num2}"
        elif choice == "4":
            if num2 == 0:
                print("Division by zero is not allowed.")
                return None
            result = num1 / num2
            operation = f"{num1} / {num2}"
        else:
            print("Invalid choice.")
            return None
        print("Result =", result)
        return operation, result
    except ValueError:
        print("Invalid input! Please enter numbers.")
        return None
# Function for Scientific Calculations
def scientific_calculation():
    try:
        num = float(input("Enter a number: "))
        print("\n1. Square Root")
        print("2. Square")
        print("3. Factorial")
        choice = input("Enter your choice: ")
        if choice == "1":
            if num < 0:
                print("Square root of a negative number is not possible.")
                return None
            result = math.sqrt(num)
            operation = f"sqrt({num})"
        elif choice == "2":
            result = math.pow(num, 2)
            operation = f"{num}²"
        elif choice == "3":
            result = math.factorial(int(num))
            operation = f"{int(num)}!"
        else:
            print("Invalid choice.")
            return None
        print("Result =", result)
        return operation, result
    except ValueError:
        print("Invalid input.")
        return None
# Function to Generate Random Number
def generate_random():
    number = random.randint(1, 100)
    print("Random Number =", number)
    return "Random Number", number
# Main Program
while True:
    print("\n===== Smart Calculator & Data Manager =====")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculations")
    print("3. Generate Random Number")
    print("4. Store Last Result")
    print("5. View History")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        last_result = basic_arithmetic()
    elif choice == "2":
        last_result = scientific_calculation()
    elif choice == "3":
        last_result = generate_random()
    elif choice == "4":
        if 'last_result' in locals() and last_result is not None:
            history[f"Result {count}"] = str(last_result)
            count += 1
            print("Result stored successfully.")
        else:
            print("No result available to store.")
    elif choice == "5":
        if history:
            print("\n----- Stored History -----")
            for key, value in history.items():
                print(key, ":", value)
        else:
            print("History is empty.")
    elif choice == "6":
        print("Thank you for using Smart Calculator!")
        break
    else:
        print("Invalid choice. Please try again.")
