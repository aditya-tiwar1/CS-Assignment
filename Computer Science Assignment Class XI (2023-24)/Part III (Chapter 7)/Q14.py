# Program to generate three random integers between 100 and 999 that are divisible by 5
import random

numbers = []
count = 0

while count < 3:
    number = random.randint(100, 999)
    if number % 5 == 0:
        numbers.append(number)
        count += 1

print("Generated numbers divisible by 5:", numbers)

# Output: Random integers divisible by 5: [generated numbers]