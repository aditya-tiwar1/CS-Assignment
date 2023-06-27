# Question 12: Identify Triangle Type

# Ask the user to input the lengths of the triangle sides
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Check if the sides form a triangle
if (a + b > c) and (b + c > a) and (c + a > b):
    # Check the type of triangle
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or c == a:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a Triangle")

# Output:
# Enter the length of side a: 4
# Enter the length of side b: 4
# Enter the length of side c: 4
# Equilateral Triangle
