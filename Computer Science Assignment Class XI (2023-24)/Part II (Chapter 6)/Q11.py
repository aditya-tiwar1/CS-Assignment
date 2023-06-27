# Question 11
# Compute simple interest and compound interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time in years: "))

simple_interest = (principal * rate * time) / 100
compound_interest = principal * ((1 + (rate / 100)) ** time - 1)

print("Simple Interest:", simple_interest)
print("Compound Interest:", compound_interest)

# Output:
# Simple Interest: <Simple Interest>
# Compound Interest: <Compound Interest>
