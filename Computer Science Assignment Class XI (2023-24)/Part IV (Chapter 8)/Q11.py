# Question 11: Find Average of Numbers

# Ask the user to enter numbers separated by spaces
numbers = input("Enter numbers separated by spaces: ")

# Split the input string into a list of numbers
number_list = numbers.split()

# Convert the list of strings to a list of integers
number_list = [int(num) for num in number_list]

# Calculate the average
average = sum(number_list) / len(number_list)

# Print the average
print("Average:", average)

# Output:
# Enter numbers separated by spaces: 10 15 20 25 30
# Average: 20.0
