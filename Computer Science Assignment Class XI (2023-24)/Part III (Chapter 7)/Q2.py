# Program to calculate the average temperature of the week
temperatures = []

for day in range(1, 8):
    temperature = float(input(f"Enter temperature for Day {day}: "))
    temperatures.append(temperature)

average_temperature = sum(temperatures) / len(temperatures)

print("Average temperature of the week:", average_temperature)

# Output: Average Temperature: [calculated value]