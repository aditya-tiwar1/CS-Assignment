# Program to reverse a 2-digit number
number = int(input("Enter a 2-digit number: "))

reversed_number = (number % 10) * 10 + number // 10

print("Reversed number:", reversed_number)

# Output: Reversed number: [reversed number]