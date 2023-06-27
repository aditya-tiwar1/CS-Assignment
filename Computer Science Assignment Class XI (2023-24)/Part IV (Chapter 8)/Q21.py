# Question 20b: Sum of Squares

# Input the value of n
n = int(input("Enter the value of n: "))

# Initialize the sum
total_sum = 0

# Compute the sum of squares
for i in range(1, n+1):
    total_sum += i ** 2

# Print the total sum
print("Total Sum:", total_sum)

# Output:
# Enter the value of n: 5
# Total Sum: 55
