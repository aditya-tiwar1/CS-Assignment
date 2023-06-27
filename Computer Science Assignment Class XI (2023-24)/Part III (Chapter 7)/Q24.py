# Program to calculate the amount payable after compound interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))

amount_payable = principal * (1 + rate) ** time

print("Amount payable after compound interest:", amount_payable)
# Output: Amount payable after compound interest: [calculated value]
