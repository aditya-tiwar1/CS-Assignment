# Program to convert seconds to minutes and seconds
seconds = int(input("Enter the number of seconds: "))

minutes = seconds // 60
remaining_seconds = seconds % 60

print(f"{seconds} seconds = {minutes} mins and {remaining_seconds} seconds")

# Output: [calculated value] seconds is [calculated value] minutes and [calculated value] seconds.