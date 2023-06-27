# Question 7: Convert Digit to Words

# Ask the user to input a digit
digit = int(input("Enter a digit (0-9): "))

# Define a list of words for each digit
digit_words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

# Check if the input is a valid digit
if 0 <= digit <= 9:
    # If valid, print the word corresponding to the digit
    print(f"The digit {digit} is written as {digit_words[digit]}.")
else:
    # If invalid, print Invalid digit
    print("Invalid digit")

# Output:
# Enter a digit (0-9): 5
# The digit 5 is written as Five.
