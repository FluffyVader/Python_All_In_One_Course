# Exercise 9: Create a copy of a list
# Create a copy of a list [10, 20, 30] and modify the copy. Print both the original and the copied list to demonstrate they are independent.
#

list2 = [10, 20, 30]
# def independent(to_add):
#     copy_list1 = list2

#     copy_list1.append(to_add)

#     print(copy_list1)
# print(list2)
##########################
l2 = list(list2)
l2.append(40)

print(list2)
print(l2)
##########################
l3 = list2.copy()
l3.append(40)

print(list2)
print(l3)
##########################
l4 = list2[::]
l4.append(40)

print(list2)
print(l4)