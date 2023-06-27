# Question 15
# Read three numbers and swap the first two variables with the sums of first and second, second and third numbers respectively

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

num1, num2 = num1 + num2, num2 + num3
print("Swapped values:")
print("First number:", num1)
print("Second number:", num2)
print("Third number:", num3)

# Output:
# Swapped values:
# First number: <Sum of First and Second Numbers>
# Second number: <Sum of Second and Third Numbers>
# Third number: <Third Number>