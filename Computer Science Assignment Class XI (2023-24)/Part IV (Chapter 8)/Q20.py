# Question 20 (a): Sum of Fractions

# Set the number of terms
terms = 7

# Initialize the numerator and denominator
numerator = 2
denominator = 9

# Initialize the sum
total_sum = 0

# Compute the sum of the fractions
for i in range(terms):
    fraction = numerator / denominator
    total_sum += fraction

    # Update the numerator and denominator
    numerator += 3
    denominator += 4

# Print the total sum
print("Total Sum:", total_sum)

# Output:
# Total Sum: 1.1045070754716981

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

