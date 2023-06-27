# Question 23a: Sum of Series - Factorial

# Input the value of x
x = int(input("Enter the value of x: "))

# Input the number of terms
n = int(input("Enter the number of terms: "))

# Initialize the sum
total_sum = 0

# Compute the sum of the series
for i in range(1, n+1):
    total_sum += (x ** i) / math.factorial(i)

# Print the total sum
print("Total Sum:", total_sum)

# Output:
# Enter the value of x: 2
# Enter the number of terms: 6
# Total Sum: 7.266666666666667

# Question 23b: Sum of Series - Power

# Input the value of x
x = int(input("Enter the value of x: "))

# Input the value of n
n = int(input("Enter the value of n: "))

# Initialize the sum
total_sum = 0

# Compute the sum of the series
for i in range(n+1):
    total_sum += (x ** i) / i

# Print the total sum
print("Total Sum:", total_sum)

# Output:
# Enter the value of x: 2
# Enter the value of n: 5
# Total Sum: 11.416666666666666
