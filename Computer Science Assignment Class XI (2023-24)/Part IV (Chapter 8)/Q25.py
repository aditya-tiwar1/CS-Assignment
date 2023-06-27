# Question 25 (a): Print alphabetical Left triangle pattern

n = 6
for i in range(n):
    for j in range(i+1):
        print(chr(j + 65), end="")
    print()

# Output: 
# A
# AB
# ABC
# ABCD
# ABCDE
# ABCDEF


# Question 25 (b): a-bb-ccc-dddd Pattern up to n lines
n = 5
a = 65

for i in range(1,n+1):
    for j in range(1, i+1):
        print("%c" %(a), end="")
    a +=1
    print()

# Output: 
# A
# BB
# CCC
# DDDD
# EEEEE

# Question 25 (c): 0-22-444-6666-88888 Pattern up to n lines

for i in range(0, 10, 2):
    for j in range(0, i + 1, 2) :
        print(i, end = ' ')
    print()

# Output: 
# 0 
# 2 2 
# 4 4 4
# 6 6 6 6
# 8 8 8 8 8

# Question 25 (d) : 2-44-666-8888 Pattern up to n lines

for i in range(2, 10, 2):
    for j in range(2, i + 1, 2) :
        print(i, end = ' ')
    print()

# Output: 
# 2 
# 4 4 
# 6 6 6 
# 8 8 8 8 