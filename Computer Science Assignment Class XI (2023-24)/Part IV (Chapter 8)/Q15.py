# Question 15: Find Largest Number

# Ask the user to enter numbers separated by spaces
numbers = input("Enter numbers separated by spaces: ")

# Split the input string into a list of numbers
number_list = numbers.split()

# Convert the list of strings to a list of integers
number_list = [int(num) for num in number_list]

# Find the largest number
largest_number = max(number_list)

# Print the largest number
print("Largest Number:", largest_number)

# Output:
# Enter numbers separated by spaces: 10 15 20 5 25
# Largest Number: 25
