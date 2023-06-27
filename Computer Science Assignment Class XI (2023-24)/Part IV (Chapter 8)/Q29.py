# Question 29: Temperature Message

# Input the temperature in Celsius
temperature = float(input("Enter the temperature in Celsius: "))

if temperature < -273.15:
    print("The temperature is invalid because it is below absolute zero.")
elif temperature == -273.15:
    print("The temperature is absolute 0.")
elif temperature < 0:
    print("The temperature is below freezing.")
elif temperature == 0:
    print("The temperature is at the freezing point.")
elif temperature < 100:
    print("The temperature is in the normal range.")
elif temperature == 100:
    print("The temperature is at the boiling point.")
else:
    print("The temperature is above the boiling point.")

# Output:
# Enter the temperature in Celsius: 25
# The temperature is in the normal range.
