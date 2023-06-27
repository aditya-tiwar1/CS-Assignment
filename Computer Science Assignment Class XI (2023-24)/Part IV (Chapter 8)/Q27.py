# Question 27: Sort Three Numbers in Ascending Order

# Input the three numbers
A = int(input("Enter the value for A: "))
B = int(input("Enter the value for B: "))
C = int(input("Enter the value for C: "))

# Find the smallest, next higher, and highest numbers
smallest = min(A, B, C)
highest = max(A, B, C)
next_higher = A + B + C - smallest - highest

# Print the sorted numbers
print("Smallest number =", smallest)
print("Next higher number =", next_higher)
print("Highest number =", highest)

# Output:
# Enter the value for A: 12
# Enter the value for B: 10
# Enter the value for C: 15
# Smallest number = 10
# Next higher number = 12
# Highest number = 15
