# Question 9: Print First n Odd Numbers in Descending Order

# Ask the user for the value of n
n = int(input("Enter the value of n: "))

# Initialize an empty list to store the odd numbers
odd_numbers = []

# Generate the odd numbers and add them to the list
for num in range(1, 2 * n + 1, 2):
    odd_numbers.append(num)

# Print the odd numbers in descending order
odd_numbers.reverse()
print("First", n, "odd numbers in descending order:", odd_numbers)

# Output:
# Enter the value of n: 5
# First 5 odd numbers in descending order: [9, 7, 5, 3, 1]
