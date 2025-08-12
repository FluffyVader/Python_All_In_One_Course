# Exercise 3: Sum and average of all numbers in a list
# Calculate and print the sum and average of all numbers in a list.

# Given:

# my_list = [10, 20, 30, 40, 50]
# Expected Output:

# Sum: 150
# Average: 30.0

class MyCustomError(Exception):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code
        super().__init__(message)

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"


list1 = [10, 20, 30, 40, 50]
sum_of_list = 0
try:
    if (len(list1) == 0):
        raise MyCustomError("The length can not be 0", -1)
    else:
        sum_of_list = sum(list1)
        print(f"Sum of list1 is: {sum_of_list}")
except MyCustomError as e:
    print(f"Can not calculate Sum, {e}")




try:
    avg_of_list = sum_of_list / len(list1)
    print(f"Avg of list1 is: {avg_of_list}")
except ZeroDivisionError as e:
    print(f"The length can not be 0. Can not calculate Average, {e}")

