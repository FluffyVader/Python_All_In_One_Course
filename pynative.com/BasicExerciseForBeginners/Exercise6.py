# Exercise 6: Display numbers divisible by 5
# Write a Python code to display numbers from a list divisible by 5

# Expected Output:

# Given list is  [10, 20, 33, 46, 55]
# Divisible by 5
# 10
# 20
# 55

def divisable_by_5_or_not(list_to_divide):
    remainder = 0

    for index in range(0, len(list_to_divide), 1):
        remainder = list_to_divide[index] % 5

        if remainder == 0:
            print(list_to_divide[index])

divisable_by_5_or_not([10, 23, 40, 55])
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
divisable_by_5_or_not([0])
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
divisable_by_5_or_not([])
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
divisable_by_5_or_not([5555555555])