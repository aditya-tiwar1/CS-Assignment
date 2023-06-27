# Question 5: Check Leap Year

# Ask the user for a year
year = int(input("Enter a year: "))

# Check the conditions for a leap year
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    # If leap year, print Leap Year
    print("Leap Year")
else:
    # If not leap year, print Not a Leap Year
    print("Not a Leap Year")

# Output:
# Enter a year: 2020
# Leap Year
