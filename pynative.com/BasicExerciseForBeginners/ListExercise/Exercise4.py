# Exercise 4: Reverse a list
# Given:


# list1 = [100, 200, 300, 400, 500]
# Expected output:

# [500, 400, 300, 200, 100]
def custom_reverse_list(list_to_reverse):
    half_list_lenght = len(list_to_reverse) // 2
    first_index = 0
    last_index = len(list_to_reverse) - 1
    
    while(first_index < half_list_lenght):
        temp_first = list_to_reverse[first_index]
        list_to_reverse[first_index] = list_to_reverse[last_index]
        list_to_reverse[last_index] = temp_first

        first_index += 1
        last_index -= 1


list1 = [100, 200, 300, 400, 500]

list1.reverse()
custom_reverse_list(list1)
assert(list1 == [100, 200, 300, 400, 500])
print(list1)