# Exercise 10: Merge two lists using the following condition
# Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the 
# second list.

# Given:

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# Expected Output:

# result list: [25, 35, 40, 60, 90]

def even_odd_numbers(list1, list2):
    calc_result = []

    for index_list1 in range(0, len(list1), 1):
        if list1[index_list1] % 2 == 1:
            calc_result.append(list1[index_list1])

    for index_list2 in range(0, len(list2),  1):
        if list2[index_list2] % 2 == 0:
            calc_result.append(list2[index_list2])


    print(calc_result)

 
even_odd_numbers([10, 20, 25, 30, 35],[40, 45, 60, 75, 90] )
even_odd_numbers([10],[12] )
