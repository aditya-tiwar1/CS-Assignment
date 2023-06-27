# Program to calculate (a + b)³ using the formula a³ + b³ + 3a²b + 3ab²
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

result = a ** 3 + b ** 3 + 3 * a ** 2 * b + 3 * a * b ** 2

print("(a + b)³:", result)
# Output: (a + b)³: [calculated value]
