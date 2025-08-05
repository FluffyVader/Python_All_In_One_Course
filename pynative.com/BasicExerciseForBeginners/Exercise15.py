# Exercise 15: Get an int value of base raises to the power of exponent
# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

# Note here exp is a non-negative integer, and the base is an integer.

# Expected output

# Case 1:

# base = 2
# exponent = 5

# 2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)
# Case 2:

# base = 5
# exponent = 4

# 5 raises to the power of 4 is: 625 
# i.e. (5 *5 * 5 *5 = 625)


def powerV1(num_to_power, num_to_power_by):
    result = num_to_power ** num_to_power_by

    print(f"{num_to_power} powered by {num_to_power_by} is {result}")

powerV1(20, 2)

def powerV2(base, exponent):
    result = 0

    #result * result * base

    for i in range(0, exponent, 1):
        result = base * base

    print(f"{base} powered by {exponent} is {result}")

powerV2(20, 2)