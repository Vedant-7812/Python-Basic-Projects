#Q.9)
# Program to extract unique words from a sentence
import math
try:
    # Take sentence input
    sentence = input("Enter a sentence: ")
    # Check for empty input
    if sentence.strip() == "":
        raise ValueError("Sentence cannot be empty.")
    # Convert sentence to lowercase and split into words
    words = sentence.lower().split()
    # Store unique words in a set
    unique_words = set(words)
    # Sort the unique words
    sorted_words = sorted(unique_words)
    # Display unique words
    print("\nUnique Words (Sorted):")
    for word in sorted_words:
        print(word)
    # Calculate square of total unique words
    count = len(unique_words)
    result = math.pow(count, 2)
    print("\nTotal Unique Words:", count)
    print("Square of Total Unique Words:", int(result))
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
