# Lambda function to calculate the square of a number
square = lambda x: x * x
try:
    # Generate numbers from 1 to 20
    numbers = range(1, 21)
    # Store squares in a list using lambda
    square_list = list(map(square, numbers))
    print("Squares of numbers from 1 to 20:")
    print(square_list)
    # Print only even squares
    print("\nEven Squares:")
    for num in square_list:
        if num % 2 == 0:
            print(num, end=" ")
except Exception as e:
    print("An error occurred:", e)
