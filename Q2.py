#Q.2)
# Function to analyze a string
def analyze_string(s):
    # Check for empty string
    if s.strip() == "":
        print("Error: Empty string is not allowed.")
        return
    # Length of string
    print("\nLength of the string:", len(s))
    # Reverse string
    print("Reversed string:", s[::-1])
    # Count vowels
    vowels = "aeiou"
    count = 0
    for ch in s.lower():
        if ch in vowels:
            count += 1
    print("Number of vowels:", count)
    # Print characters with positive and negative index
    print("\nCharacter Positions:")
    for i in range(len(s)):
        print(f"Positive Index: {i}, Negative Index: {i - len(s)}, Character: {s[i]}")
# Main Program
text = input("Enter a string: ")
analyze_string(text)
