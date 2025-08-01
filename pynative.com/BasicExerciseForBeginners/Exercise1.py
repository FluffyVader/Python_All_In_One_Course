"""
Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

Given 1:

number1 = 20
number2 = 30
Expected Output:

The result is 600
Given 2:

number1 = 40
number2 = 30
Expected Output:

The result is 70
"""


def product_or_sum(number1, number2):
    sum_or_product_number = number1 * number2

    if sum_or_product_number > 1000:
        sum_or_product_number = number1 + number2

    return sum_or_product_number

    # product = number1 * number2
    # if product <= 1000:
    #     return product
    # return number1 + number2

result = product_or_sum(20, 30)
print(f"the result is: {result}")
assert result == 600

result = product_or_sum(30, 40)
print(f"the result is: {result}")
assert result == 70

result = product_or_sum(20, 50)
print(f"the result is: {result}")
assert result == 1000

result = product_or_sum(-20, 50)
print(f"the result is: {result}")
assert result == -1000

result = product_or_sum(-30, -50)
print(f"the result is: {result}")
assert result == -80