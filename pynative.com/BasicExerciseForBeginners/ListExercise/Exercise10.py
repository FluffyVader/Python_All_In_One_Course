# Exercise 10: Combine two lists
# Combine given two lists into a single list and print it.

# Given:

# list_a = [1, 2]
# list_b = [3, 4]
# Expected Output:

# [1, 2, 3, 4]

list_a = [1, 2]
list_b = [3, 4]

combined_list = list_a + list_b
print(combined_list)
########################################
list_c = [1, 2]
list_d = [3, 4]

list_c.extend(list_d)
print(list_c)
########################################
combined_list3 = [*list_a, *list_b]

print(combined_list3)