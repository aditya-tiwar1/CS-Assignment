# Question 24(a): Diamond shape

for i in range(1, 4):
    print(' ' * (3 - i), '*' * (2 * i - 1))
for i in range(2, 0, -1):
    print(' ' * (3 - i), '*' * (2 * i - 1))

# Output:
#   *
#  ***
# *****
#  ***
#   *

# Question 24 (b): Python star pattern to print right pascal triangle
def pattern(n):
   for i in range(n):
      print('* ' * (i + 1))
   for i in range(n):
      print('* ' * (n - i - 1))
 
# function call
pattern(3)

# Question 24(c): Hollow Diamond shape with width 3 stars

for i in range(1, 4):
    print(' ' * (3 - i) + '*' + ' ' * (2 * i - 3) + ('*' if i > 1 else ''))
for i in range(2, 0, -1):
    print(' ' * (3 - i) + '*' + ' ' * (2 * i - 3) + ('*' if i > 1 else ''))

# Output:
#   *
#  * *
# *   *
#  * *
#   *

# Question 24 (d): Python star pattern to print hollow right pascal triangle

rows = 4

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print('*', end = '')
        else:
            print(end = ' ')      
    print()

for i in range(1, rows + 1):
    for j in range(rows - 1, i - 1, -1):
        if j == rows - 1 or j == i or i == rows:
            print('*', end = '')
        else:
            print(end = ' ')
    for k in range(1, i):
        print(end = ' ')
    print()