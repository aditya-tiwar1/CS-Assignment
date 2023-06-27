# Program to generate six random numbers and calculate their mean, median, and mode
import random
from statistics import mean, median, mode

numbers = [random.randint(0, 9) for _ in range(6)]

mean_value = mean(numbers)
median_value = median(numbers)
mode_value = mode(numbers)

print("Generated numbers:", numbers)
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)

# Output:
# Numbers: [random numbers]
# Mean: [calculated value]
# Median: [calculated value]
# Mode: [calculated value]