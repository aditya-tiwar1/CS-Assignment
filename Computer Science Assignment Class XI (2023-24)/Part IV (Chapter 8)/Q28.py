# Question 28: Temperature Conversion

# Input the temperature
temperature = float(input("Enter the temperature: "))

# Input the unit of the temperature
unit = input("Enter the unit of the temperature (C/F): ")

if unit == 'C':
    # Convert Celsius to Fahrenheit
    converted_temp = (9/5) * temperature + 32
    converted_unit = 'Fahrenheit'
elif unit == 'F':
    # Convert Fahrenheit to Celsius
    converted_temp = (5/9) * (temperature - 32)
    converted_unit = 'Celsius'
else:
    print("Invalid unit!")
    exit()

# Print the converted temperature
print("Converted temperature:", converted_temp, converted_unit)

# Output:
# Enter the temperature: 25
# Enter the unit of the temperature (C/F): C
# Converted temperature: 77.0 Fahrenheit
