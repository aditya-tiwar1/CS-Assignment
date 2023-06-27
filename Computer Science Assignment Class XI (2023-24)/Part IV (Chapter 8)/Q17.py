# Question 17: Palindrome Numbers

# Function to check if a number is palindrome
def is_palindrome(number):
    # Convert the number to a string
    number_str = str(number)
    # Check if the string is equal to its reverse
    if number_str == number_str[::-1]:
        return True
    else:
        return False

# Given list of integers
numbers = [12321, 45654, 78987, 12345, 54321]

# Find palindromes from the list
palindromes = [num for num in numbers if is_palindrome(num)]

# Print the palindromes
for palindrome in palindromes:
    print(palindrome)

# Output:
# 12321
# 45654
# 78987
# 54321
