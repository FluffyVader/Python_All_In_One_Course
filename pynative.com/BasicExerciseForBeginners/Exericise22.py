# Exercise 22: Capitalize the first letter of each word in a string
# Expected Output:

# str1 = "pynative.com is for python lovers"
# Output Pynative.com Is For Python Lovers

str_to_capitalize = "pynative.com is for python lovers"

for first_symbol in str_to_capitalize:
    str_to_capitalize = str_to_capitalize.title()

print(str_to_capitalize)