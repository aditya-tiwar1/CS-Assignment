# Question 19: Divisible by m

# Read the values of n and m
n = int(input("Enter the value of n: "))
m = int(input("Enter the value of m: "))

# Print every integer between 1 and n divisible by m
for num in range(1, n+1):
    if num % m == 0:
        # Check if the number is even or odd
        if num % 2 == 0:
            print(num, "is divisible by", m, "and is even")
        else:
            print(num, "is divisible by", m, "and is odd")

# Output:
# Enter the value of n: 20
# Enter the value of m: 3
# 3 is divisible by 3 and is odd
# 6 is divisible by 3 and is even
# 9 is divisible by 3 and is odd
# 12 is divisible by 3 and is even
# 15 is divisible by 3 and is odd
# 18 is divisible by 3 and is even
