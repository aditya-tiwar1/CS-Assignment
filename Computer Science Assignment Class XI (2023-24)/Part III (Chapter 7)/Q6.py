# Program to check if the first number is fully divisible by the second number
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 % num2 == 0:
    print(num1, "is fully divisible by", num2)
else:
    print(num1, "is not fully divisible by", num2)

# Output: [First number] is fully divisible by [Second number]. (or) [First number] is not fully divisible by [Second number].