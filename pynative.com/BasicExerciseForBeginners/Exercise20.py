# Exercise 20: Print Reverse Number Pattern
# Expected Output:

# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5 

#down ward triangle made out of numbers

for i in range(1, 6, 1):
    for j in range(0, 6-i, 1):
        print(i, end = " ")
    
    print("")