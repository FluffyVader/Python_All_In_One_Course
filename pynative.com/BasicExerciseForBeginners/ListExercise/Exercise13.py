# Exercise 13: Remove all occurrences of a specific item from a list
# Given a Python list, write a program to remove all occurrences of item 20.

# Given:

# list1 = [5, 20, 15, 20, 25, 50, 20]

#############################################################################

def custom_remove(thing_to_remove, list1):
    for item in list1:
        if item == thing_to_remove:
            list1.remove(item)

#############################################################################

list_to_process = [5, 20, 15, 20, 25, 50, 20]

print(list_to_process)
custom_remove(20, list_to_process)

print(list_to_process)

#############################################################################
#remove will only remove 1 item never use this
list_to_process = [5, 20, 15, 20, 25, 50, 20]
print(list_to_process)
list_to_process.remove(20)
print(list_to_process)

#############################################################################