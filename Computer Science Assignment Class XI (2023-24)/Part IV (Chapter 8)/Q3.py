# Question 3: Calculate Time after Given Hours

# Ask the user for the current hour and the number of hours ahead
current_hour = int(input("Enter the current hour (1-12): "))
hours_ahead = int(input("Enter the number of hours ahead: "))

# Calculate the new hour by adding the current hour and hours ahead,
# and take the modulo 12 to handle values over 12
new_hour = (current_hour + hours_ahead) % 12

# Print the new hour
print(f"The time after {hours_ahead} hours will be {new_hour} o'clock.")

# Output:
# Enter the current hour (1-12): 9
# Enter the number of hours ahead: 4
# The time after 4 hours will be 1 o'clock.
