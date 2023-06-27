# Question 8
# Convert height in centimeters to feet and inches

height_cm = float(input("Enter your height in centimeters: "))
height_feet = height_cm / 30.48  # Convert to feet
height_inches = height_cm / 2.54  # Convert to inches
print("Your height is:", int(height_feet), "feet", int(height_inches), "inches")

# Output:
# Your height is: <Feet> feet <Inches> inches

