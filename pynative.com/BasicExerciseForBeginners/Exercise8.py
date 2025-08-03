# Exercise 8: Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5
# Refer:

# Print Pattern using for loop
# Nested loops in Python

for i in range(1, 6, 1):
    for j in range(0, i, 1):
        print(i, end = " ")
    
    print("")

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-")

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3 
# 4 4
# 5

for i in range(1, 6, 1):
    for j in range(0, 6-i, 1):
        print(i, end = " ")
    
    print("")

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-")
# 5 
# 4 4 
# 3 3 3 
# 2 2 2 2 
# 1 1 1 1 1 

for i in range(5, 0, -1):
    for j in range(0, 6-i, 1):
        print(i, end = " ")
    
    print("")

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-")
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3 
# 2 2 
# 1

for i in range(5, 0, -1):
    for j in range(0, i, 1):
        print(i, end = " ")
    
    print("")

