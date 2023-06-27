# Question 4: Check if Numbers are Close

# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check if the absolute difference between the numbers is less than 0.001
if abs(num1 - num2) < 0.001:
    # If close, print Close
    print("Close")
else:
    # If not close, print Not close
    print("Not close")

# Output:
# Enter the first number: 3.14
# Enter the second number: 3.139
# Close
