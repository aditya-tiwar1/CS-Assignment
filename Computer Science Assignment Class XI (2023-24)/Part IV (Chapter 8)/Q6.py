# Question 6: Check Triangle Validity

# Ask the user for the lengths of the three sides of the triangle
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Check the triangle validity condition
if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    # If valid triangle, print Triangle is valid
    print("Triangle is valid")
else:
    # If not a valid triangle, print Triangle is not valid
    print("Triangle is not valid")

# Output:
# Enter the length of side 1: 3
# Enter the length of side 2: 4
# Enter the length of side 3: 5
# Triangle is valid
