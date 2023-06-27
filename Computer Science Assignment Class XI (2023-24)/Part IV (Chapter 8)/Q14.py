# Question 13: Check Ending Digit

# Ask the user to input an integer
num = int(input("Enter an integer: "))

# Check the ending digit
last_digit = num % 10

if last_digit == 4:
    print("Ends with 4")
elif last_digit == 8:
    print("Ends with 8")
else:
    print("Ends with neither")

# Output:
# Enter an integer: 452
# Ends with 2
