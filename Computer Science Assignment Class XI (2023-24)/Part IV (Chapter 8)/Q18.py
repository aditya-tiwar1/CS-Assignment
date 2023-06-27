# Question 18: Manipulate Digits

# Read an integer X
X = int(input("Enter an integer: "))

# Determine the number of digits n in X
n = len(str(X))

# Form an integer Y that has the number of digits n at ten's place
# and the most significant digit of X at one's place
Y = (n * 10) + int(str(X)[0])

# Output Y
print("Output Y:", Y)

# Output:
# Enter an integer: 2134
# Output Y: 42
