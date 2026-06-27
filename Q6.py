#Q.6)
# Program using Sets, Tuples, random module, and math module
import random
import math
try:
    numbers = set()
    print("Enter 10 numbers:")
    # Take 10 numbers as input
    while len(numbers) < 10:
        num = int(input(f"Enter number {len(numbers) + 1}: "))
        numbers.add(num)
    # Convert set to tuple
    number_tuple = tuple(numbers)
    print("\nUnique Numbers (Set):", numbers)
    print("Tuple:", number_tuple)
    # Pick 3 random numbers from the tuple
    random_numbers = random.sample(number_tuple, 3)
    print("3 Random Numbers:", random_numbers)
    # Find square root of the sum of tuple elements
    total = sum(number_tuple)
    square_root = math.sqrt(total)
    print("Sum of Tuple Elements:", total)
    print("Square Root of Sum:", round(square_root, 2))
except ValueError:
    print("Invalid input! Please enter only integers.")
except Exception as e:
    print("An error occurred:", e)
