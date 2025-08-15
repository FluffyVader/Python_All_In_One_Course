# Exercise 12: Remove Duplicates from list
# Write a function that takes a list with duplicate elements and returns a new list with only unique elements.

# Given: list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]

# Expected Output:

# [1, 2, 3, 4, 5]
#################################################################
def remove_duplicates(list_with_duplicates_local):
    dictionary = dict()

    for item in list_with_duplicates_local:
        if item not in dictionary.keys():
            dictionary[item] = 0
        
        dictionary[item] = dictionary[item] + 1

    list_with_duplicates_local.clear()
    for key_as_list_item, number_of_duplicates in dictionary.items():
        if number_of_duplicates > 1:
            list_with_duplicates_local.append(key_as_list_item)    


    print(dictionary)
    print(list_with_duplicates_local)


list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]

mydict = dict.fromkeys(list_with_duplicates)
list_with_out_duplicates = list(mydict)

print(f"List with duplicates{list_with_duplicates}")
print(f"List without duplicates{list_with_out_duplicates}")

print("=============================")
remove_duplicates(list_with_duplicates)
#print(f"List without duplicates{list_with_out_duplicates}")
