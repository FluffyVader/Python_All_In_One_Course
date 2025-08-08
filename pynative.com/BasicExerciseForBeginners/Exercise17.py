# Exercise 17: Generate Fibonacci series up to 15 terms
# Have you ever wondered about the Fibonacci Sequence? It’s a series of numbers in which the next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.

# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series is 13 + 21 = 34.

# Expected output:

# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34  55  89  144  233  377
# Refer: Generate Fibonacci Series in Python

##############################################################################

def fibonacci(term):
    Fn_2 = 0
    Fn_1 = 1
    
    print(f"Fibonacci sequence: {term}:")

    if term < 3:
        print("Sorry, you can't give the function an agrument that is smaller then 3")
        print("-----------------------------------------------------------------")
        return
    
    print(Fn_2, end =" ")
    print(Fn_1, end =" ")
    

    F_curr = 0
    for i in range(3, term+1, 1):
        F_curr = Fn_1 + Fn_2

        Fn_2 = Fn_1
        Fn_1 = F_curr

        print(F_curr, end =" ")

    print("\n-----------------------------------------------------------------")

##############################################################################


fibonacci(15)
fibonacci(3)
fibonacci(2)
fibonacci(1)
fibonacci(-1)
fibonacci(150)

