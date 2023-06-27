# Program to find the length of a side of a right-angled triangle
import math

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))

angle = math.radians(float(input("Enter the angle in degrees: ")))

side3 = math.sqrt(side1 ** 2 + side2 ** 2 - 2 * side1 * side2 * math.cos(angle))

print("Length of the third side:", side3)

# Output: Length of side 3: [calculated value]