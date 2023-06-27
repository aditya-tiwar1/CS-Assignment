# Program to calculate the number of days, hours, minutes, and seconds in a given number of years
years = float(input("How many years? "))

days = years * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"{years} years is:")
print(f"{days} days")
print(f"{hours} hours")
print(f"{minutes} minutes")
print(f"{seconds} seconds")

# Output:
# [years] years is:
# [days] days
# [hours] hours
# [minutes] minutes
# [seconds] seconds