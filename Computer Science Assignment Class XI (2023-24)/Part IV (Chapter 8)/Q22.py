# Question 22: Count Employees in Age Groups

# Input the number of employees
n = int(input("Enter the number of employees: "))

# Initialize the count for each age group
count_26_35 = 0
count_36_45 = 0
count_46_55 = 0

# Input the age of each employee and update the counts
for i in range(n):
    age = int(input(f"Enter the age of employee {i+1}: "))

    if 26 <= age <= 35:
        count_26_35 += 1
    elif 36 <= age <= 45:
        count_36_45 += 1
    elif 46 <= age <= 55:
        count_46_55 += 1

# Print the counts
print("Number of employees in age group 26-35:", count_26_35)
print("Number of employees in age group 36-45:", count_36_45)
print("Number of employees in age group 46-55:", count_46_55)

# Output:
# Enter the number of employees: 5
# Enter the age of employee 1: 30
# Enter the age of employee 2: 40
# Enter the age of employee 3: 50
# Enter the age of employee 4: 25
# Enter the age of employee 5: 35
# Number of employees in age group 26-35: 3
# Number of employees in age group 36-45: 1
# Number of employees in age group 46-55: 1
