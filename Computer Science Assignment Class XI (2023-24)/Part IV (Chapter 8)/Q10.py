# Question 10: Print Number Series

# (i) 1 4 7 10 ........ 40
print("(i) Number Series:")
for num in range(1, 41, 3):
    print(num, end=" ")

print()

# (ii) 1 -4 7 -10 ........ -40
print("(ii) Number Series:")
for i in range(1, 41, 3):
    num = i if i % 2 != 0 else -i
    print(num, end=" ")

# Output:
# (i) Number Series:
# 1 4 7 10 13 16 19 22 25 28 31 34 37 40
# (ii) Number Series:
# 1 -4 7 -10 13 -16 19 -22 25 -28 31 -34 37 -40
