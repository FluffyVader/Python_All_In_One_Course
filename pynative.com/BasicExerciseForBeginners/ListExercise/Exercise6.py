# Exercise 6: Find Maximum and Minimum
# Find and print the largest and smallest number in a list [8, 2, 15, 1, 9].

# Given:

# data = [8, 2, 15, 1, 9]

# Expected Output:

# Largest number: 15
# Smallest number: 1

def custom_max(list1):
    MaxNumber = list1[0]
    for index in range(1, len(list1), 1):
        if list1[index] > MaxNumber:
            MaxNumber = list1[index]

    return MaxNumber

#################################################################

def custom_min(list1):
    MinNumber = list1[0]
    for index in range(1, len(list1), 1):
        if list1[index] < MinNumber:
            MinNumber = list1[index]

    return index, MinNumber

#################################################################

number_list = [8, 2, 15, 1, 9]
min_number = min(number_list)
max_number = max(number_list)

assert min_number == 1
assert max_number == 15

min_number = custom_min(number_list)[1]
max_number = custom_max(number_list)

assert min_number == 1
assert max_number == 15

print(f"The min is: {min_number} and the max is {max_number}")