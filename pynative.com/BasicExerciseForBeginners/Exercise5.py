# Exercise 5: Check if the first and last numbers of a list are the same
# Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.

# Given:

# numbers_x = [10, 20, 30, 40, 10]
# # output True

# numbers_y = [75, 65, 35, 75, 30]
# # Output False

def first_and_last_chars_same_or_not(list_of_numbers):
    #list_of_numbers = [10, 20, 30, 40, 10]

    first_index_value = 0
    last_index_value = len(list_of_numbers) - 1

    if list_of_numbers[last_index_value] == list_of_numbers[first_index_value]:
        print("The first and last values of the list are the same")
        return True

    else:
        print("The first and last values of the list are not the same")
        return False

first_and_last_chars_same_or_not([10, 20, 20, 20, 20, 30, 10, 20])