# Perform following list manipulation operations on given list

# Change Element: Change the second element of a list to 200 and print the updated list.
# Append Element: Add 600 at the end of a list and print the new list.
# Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
# Remove Element (by value): Remove 600 from the list and print the list.
# Remove Element (by index): Remove the element at index 0 from the list print the list.

# Expected Output:

# Initial list: [10, 20, 30, 40, 50]

# After changing second element: [10, 200, 30, 40, 50]
# List after appending 600: [10, 200, 30, 40, 50, 600]
# List after inserting 300 at index 2: [10, 200, 300, 30, 40, 50, 600]
# List after removing 600 (by value): [10, 200, 300, 30, 40, 50]
# List after removing element at index 0: [200, 300, 30, 40, 50]


list_to_do_things_with = [10, 20, 30, 40, 50]

list_to_do_things_with[1] = 200
assert(list_to_do_things_with == [10, 200, 30, 40, 50])
print(f"After changing second element: {list_to_do_things_with}")

list_to_do_things_with.append(600)
assert(list_to_do_things_with == [10, 200, 30, 40, 50, 600])
print(f"List after appending 600 {list_to_do_things_with}")

list_to_do_things_with.insert(2, 300)
assert(list_to_do_things_with == [10, 200, 300, 30, 40, 50, 600])
print(f"List after inserting 300 at index 2: {list_to_do_things_with}")

list_to_do_things_with.remove(600)
assert(list_to_do_things_with == [10, 200, 300, 30, 40, 50])
print(f"List after removing 600: {list_to_do_things_with}")

#del list_to_do_things_with[0]
list_to_do_things_with.pop(0)
assert(list_to_do_things_with == [200, 300, 30, 40, 50])
print(f"List after removing element at index 0: {list_to_do_things_with}")