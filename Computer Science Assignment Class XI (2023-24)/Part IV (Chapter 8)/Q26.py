# Question 26: Rectangle of Stars

# Define the number of rows and stars per row
rows = 6
stars_per_row = 20

# Loop through each row
for i in range(rows):
    # Loop to print stars in each row
    for j in range(stars_per_row):
        print('*', end='')
    print()  # Move to the next line after printing stars in a row

# Output:
# ********************
# ********************
# ********************
# ********************
# ********************
# ********************
