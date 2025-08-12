# Exercise 1: Perform Basic List Operations
# Given:

# my_list = [10, 20, 30, 40, 50]
# Perform following operations on given list

# Access Elements: Print the third element.
# List Length: Print the number of elements in the list
# Check if Empty: Write a code to check is list empty.
# Expected Output:

# Initial list: [10, 20, 30, 40, 50]

# Third item: 30
# Length of the list: 5
#list is not empty

list1 = [10, 20, 30, 40, 50]

print(f"Third item of list is: {list1[2]}")

print(f"The lenght of the list is: {len(list1)}")

if len(list1) == 0:
    print(f"This list is empty")

else:
    print(f"This list is not empty")