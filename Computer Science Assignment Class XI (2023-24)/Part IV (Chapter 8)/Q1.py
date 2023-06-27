# Question 1: Convert Centimeters to Inches

# Ask the user to enter the length in centimeters
centimeters = float(input("Enter length in centimeters: "))

# Check if the length is negative
if centimeters < 0:
    # If negative, print invalid entry
    print("Invalid entry.")
else:
    # If positive, convert centimeters to inches
    inches = centimeters / 2.54
    # Print the result with 2 decimal places
    print(f"{centimeters} centimeters is equal to {inches:.2f} inches.")

# Output:
# Enter length in centimeters: 100
# 100.0 centimeters is equal to 39.37 inches.
