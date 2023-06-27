# Question 30: Prime Factors

# Function to find the prime factors of a number
def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Input the maximum value to display
max_value = int(input("Enter the maximum value to display: "))

# Loop through each number from 1 to max_value
for num in range(1, max_value + 1):
    factors = prime_factors(num)
    factors_str = ' x '.join(map(str, factors))
    print(num, '=', factors_str if len(factors) > 1 else 'prime')

# Output:
# Enter the maximum value to display: 10
# 1 = prime
# 2 = prime
# 3 = prime
# 4 = 2 x 2
# 5 = prime
# 6 = 2 x 3
# 7 = prime
# 8 = 2 x 2 x 2
# 9 = 3 x 3
# 10 = 2 x 5
