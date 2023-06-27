# Question 8: Check Prime Square Root

import math

# Ask the user for a number
num = int(input("Enter a number: "))

# Check if the square root of the number is prime
sqrt = math.isqrt(num)
is_prime = True

if sqrt > 1:
    for i in range(2, sqrt + 1):
        if sqrt % i == 0:
            is_prime = False
            break
else:
    is_prime = False

# Print the result
if is_prime:
    print("Square root is prime")
else:
    print("Square root is not prime")

# Output:
# Enter a number: 25
# Square root is not prime
