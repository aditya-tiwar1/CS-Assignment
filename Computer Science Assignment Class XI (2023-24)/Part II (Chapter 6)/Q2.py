# Question 2
# Read today's date and display the number of days left in the current month

from datetime import date

today = date.today()
days_left = (today.replace(day=1) - today).days + today.month % 2  # Calculation for days left
print("Number of days left in the current month:", days_left)

# Output:
# Number of days left in the current month: <Number of days>


