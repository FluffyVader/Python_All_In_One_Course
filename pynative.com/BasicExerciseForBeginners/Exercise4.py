'''
Exercise 4: Remove first n characters from a string
Write a Python code to remove characters from a string from 0 to n and return a new string.

Given:

def remove_chars(word, n):
    # write your code

print("Removing characters from a string")
print(remove_chars("pynative", 4)) 
# output 'tive' first four characters are removed

print(remove_chars("pynative", 2)) 
# output 'native'
Note: n must be less than the length of the string.
'''
##########################################################################################
def remove_chars(word, num_of_letter_to_remove = 0):
    result = str()
    for index in range(0, len(word), 1):
        if index < num_of_letter_to_remove:
            continue
        result += word[index]
    
    return result
##########################################################################################


print(remove_chars("abcdefg 1", 3))

print(remove_chars("", 2))

print(remove_chars("abcdefg 1", 9))

print(remove_chars("abcdefg 1", 0))
print(remove_chars("abcd\tfg", 5))


test_str = "this_str"
number_of_symbols_to_remove = int(input(f"please enter a number of first characters to remove from '{test_str}': "))

modified_test_str = test_str[number_of_symbols_to_remove:]

print(modified_test_str)