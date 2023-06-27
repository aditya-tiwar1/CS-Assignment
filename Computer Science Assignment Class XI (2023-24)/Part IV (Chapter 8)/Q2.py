# Question 2: Calculate Total Cost of Items

# Ask the user for the number of items they are buying
num_items = int(input("Enter the number of items: "))

# Calculate the total cost based on the given conditions
if num_items < 10:
    cost = num_items * 120
elif num_items < 100:
    cost = num_items * 100
else:
    cost = num_items * 70

# Print the total cost
print(f"The total cost is {cost}.")

# Output:
# Enter the number of items: 75
# The total cost is 7500.
