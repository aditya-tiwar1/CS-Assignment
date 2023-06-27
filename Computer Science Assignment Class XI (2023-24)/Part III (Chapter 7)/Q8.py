# Program to reverse a 3-digit number
number = int(input("Enter a 3-digit number: "))

reversed_number = (number % 10) * 100 + ((number // 10) % 10) * 10 + number // 100

print("Reversed number:", reversed_number)

# Output: Reversed number: [reversed number]